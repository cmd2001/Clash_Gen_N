# upstream subscribe link parser

import requests
import yaml
from config.config import headers


def parse_upstream(url):
    text = ''
    for i in range(0, 3):
        try:
            res = requests.get(url=url, headers=headers)
        except:
            continue
        code = res.status_code
        if code == 200:
            text = res.text
            break
    if text == '':
        raise Exception
    dic = yaml.safe_load(text)
    ret = {}
    for key, value in dic.items():
        if key == 'port' or key == 'socks-port' or key == 'allow-lan' or key == 'mode' or \
                key == 'log-level' or key == 'external-controller':
            ret[key] = value
    ret['proxies'] = dic['proxies']
    return ret
