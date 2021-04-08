# generate yaml text

import yaml
import ruamel.yaml
from upstream_parser import parse_upstream
from rule_parser import RuleParser
from config.config import rules_list, url, extra_urls

def work():
    ret = {}
    # copy upstream data
    upstream = parse_upstream(url)
    for key, value in upstream.items():
        if key == 'port' or key == 'socks-port' or key == 'allow-lan' or key == 'mode' or \
                key == 'log-level' or key == 'external-controller':
            ret[key] = value

    # generate proxy list
    proxies = list(upstream['proxies'])

    for extra_url in extra_urls.split('\n'):
        if extra_url == '':
            continue
        # noinspection PyBroadException
        try:
            proxies = proxies + list(parse_upstream(extra_url)['proxies'])
        except:
            pass

    upstream_proxy_list = []
    for proxy in proxies:
        upstream_proxy_list.append(proxy['name'])

    custom_proxies_file = open('config/custom_proxies.list', 'r')
    custom_proxies = yaml.safe_load(custom_proxies_file.read())
    custom_proxies_file.close()
    if custom_proxies is not None:
        for proxy in custom_proxies:
            proxies.append(proxy)  # force override duplicated node
    proxy_list = []
    for proxy in proxies:
        proxy_list.append(proxy['name'])
    ret['proxies'] = proxies

    # generate proxy groups
    proxy_groups = []
    proxy_groups.append({'name': 'Node_A', 'type': 'select', 'proxies': ['DIRECT', 'Auto_Select_All'] + proxy_list})  # Node Select A
    proxy_groups.append({'name': 'Node_B', 'type': 'select', 'proxies': ['DIRECT', 'Auto_Select_Upstream'] + proxy_list})  # Node Select B
    proxy_groups.append({'name': 'Auto_Select_All', 'type': 'url-test', 'url': 'http://www.gstatic.com/generate_204',
                         'interval': 300, 'tolerance': 50, 'proxies': proxy_list})  # Auto Select from ALL nodes
    proxy_groups.append({'name': 'Auto_Select_Upstream', 'type': 'url-test', 'url': 'http://www.gstatic.com/generate_204',
                         'interval': 300, 'tolerance': 50, 'proxies': upstream_proxy_list})  # Auto Select from upstream nodes
    # Build two groups to avoid Auto_Select fails to work when custom proxy contains domestic nodes.

    for display_name, file_name in rules_list:  # We provide a selection from Node_A, Node_B, Auto_Select for all groups
        proxy_groups.append({'name': display_name, 'type': 'select', 'proxies': ['Node_A', 'Node_B', 'Auto_Select_All', 'Auto_Select_Upstream']})

    proxy_groups.append({'name': 'Others', 'type': 'select', 'proxies': ['Node_A', 'Node_B', 'Auto_Select_All', 'Auto_Select_Upstream']})
    ret['proxy-groups'] = proxy_groups

    # generate ruls
    rules = []
    for display_name, file_name in rules_list:
        temp_rules = RuleParser('rules/' + file_name).parse()
        for line in temp_rules:
            rules.append(line['method'] + ',' + line['domain'] + ',' + display_name)
    rules.append('MATCH,Others')
    ret['rules'] = rules

    return ruamel.yaml.dump(ret, Dumper=ruamel.yaml.RoundTripDumper)



