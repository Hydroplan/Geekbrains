import requests

site_address = 'https://github.com/elastic/examples/raw/master/' \
               'Common%20Data%20Formats/nginx_logs/nginx_logs'
site_info = requests.get(site_address)
list_with_data = site_info.text.split('\n')
result_list = []
for el in list_with_data:
    remote_addr = el[:el.find('- -') - 2]
    request_type = el[el.find('] "') + 3:el.find(' /')]
    requested_resource = el[el.find(' /') + 1:el.find('HTTP') - 1]
    result_list.append((remote_addr, request_type, requested_resource))

print(result_list[0:3])
list_of_remote_addr = []

for el in result_list:
    list_of_remote_addr.append(el[0])

max_requests = 0
for el in set(list_of_remote_addr):

    if max_requests < list_of_remote_addr.count(el):
        max_requests = list_of_remote_addr.count(el)
        max_requests_ip = el

print(f'Максимум запросов: {max_requests}, с адреса {max_requests_ip}')
