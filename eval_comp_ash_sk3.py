import time
import os
import requests
import subprocess

f = open('./res_ash_sk3/eval_final.txt','r')
r = f.read()
rl = r.split('\n\n')


dt_rate = []
cs_list = []

for i in rl:
    ts = i.split('\n')[1::]
    for j in ts:
        cs_tmp = j.split(' ')[0]
        if cs_tmp not in cs_list:
            cs_list.append(cs_tmp)
    
    tmp = i.split('\n')[0].split(' ')

    d = int(tmp[1])
    n = int(tmp[2])
    rt = n/d
    dt_rate.append(rt)

dr_avg = 0

for i in dt_rate:
    dr_avg += i

dr_avg = dr_avg / len(dt_rate)

cs_real = []

for i in cs_list:
    tmp =  i + " 0 0"
    cs_real.append(tmp)

for i in rl:
    ts = i.split('\n')[1::]
    for j in ts:
        cs_tmp = j.split(' ')[0]
        cs_res = j.split(' ')[1]
        cs_idx = cs_list.index(cs_tmp)

        if cs_res == 'None':
            continue

        cs_d = int(cs_real[cs_idx].split(' ')[1])+1
        cs_n = int(cs_real[cs_idx].split(' ')[2])

        if cs_res == 'True':
            cs_n += 1

        cs_real[cs_idx] = cs_tmp + " " + str(cs_d) + " " + str(cs_n)


dt_list = []

for i in cs_real:
    d = int(i.split(' ')[1])
    n = int(i.split(' ')[2])
    rt = dt_list.append(n/d)
    
print("avg detection rate : {}".format(dr_avg))

print("number of softwares : {}".format(len(cs_real)))

low_list = []

for i in sorted(dt_list):
    if i < 0.92:
        low_list.append(i)

print("number of softwares with lower detection rate : {}".format(len(low_list)))