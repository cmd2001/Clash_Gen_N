# Configuration file

# Your upstream clash subscribe url

url = 'https://your.subscribe.url'
extra_urls = '''
https://your.extra.subscribe.url1
https://your.extra.subscribe.url1
'''

# Request headers (you can keep this value for for most times)

headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4146.4 Safari/537.36'
}


# Rules file list, edit it as ('Display_Name', 'filename')

rules_list = (('Domestic_Sites', 'domestic.list'),
              ('DNS_Polluted', 'polluted.list'),
              ('Region_Restricted', 'region.list'),
              ('Popular_Sites', 'popular.list'),
              ('Local_Area_Network', 'lan.list'),
              ('Custom_Sites', 'custom.list'))
