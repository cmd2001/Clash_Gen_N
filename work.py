# generate yaml text

from flask import make_response
import yaml
import ruamel.yaml
from upstream_parser import parse_upstream
from config.config import urls

def work():
    ret = {}
    # copy upstream data
    sp = urls.strip().split('\n')
    upstream = parse_upstream(sp[0])
    for key, value in upstream.items():
        if key == 'port' or key == 'socks-port' or key == 'allow-lan' or key == 'mode' or \
                key == 'log-level' or key == 'external-controller':
            ret[key] = value

    # generate proxy list
    proxies = list(upstream['proxies'])

    for i in range(1, len(sp)):
        extra_url = sp[i]
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
    ret['proxy-groups'] = proxy_groups

    # generate ruls
    rules = []
    ret['rules'] = rules

    response = make_response(ruamel.yaml.dump(ret, Dumper=ruamel.yaml.RoundTripDumper), 200)
    response.mimetype = "text/plain"
    return response



