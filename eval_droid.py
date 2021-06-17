import os
import requests
import time
import subprocess
import json

from pwn import *

f = open("./res_droids/finished_decom.txt", "r")

f1 = open("./res_droids/eval_result.txt", "a")

res = f.read().split('\n')[:-1]

hash_list = []
pkg_list = []


for i in range(len(res)):
    hash_list.append(res[i].split(' ')[1])
    pkg_list.append(res[i].split(' ')[2])


api_key = 'Virustotal_api_key'


url = 'https://www.virustotal.com/vtapi/v2/file/report'


for i in range(len(hash_list)):

    params = {'apikey': api_key, 'resource': hash_list[i]}
    response = requests.get(url, params=params)
    res_json = response.json()


    if (res_json['response_code'] == 0):
        f1.write(hash_list[i] + ' ' + 'None None' + '\n\n')
        print(hash_list[i] + ' : None')
        time.sleep(16)
        continue

    total = res_json['total']
    pos = res_json['positives']
    #print(type(response.json()))
    f1.write(hash_list[i] + ' ' + str(total) + ' ' + str(pos) + '\n')

    res_json = res_json['scans']

    for key in res_json:
        f1.write(key + ' ' + str(res_json[key]['detected']) + '\n')

    f1.write('\n')

    print("{} counter : {}".format(hash_list[i], i+1))

    time.sleep(16)

