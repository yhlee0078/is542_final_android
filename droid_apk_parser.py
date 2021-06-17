# -*- coding: utf-8 -*-

import time
import os
import requests
import subprocess

from androguard.core.bytecodes import apk
from androguard.core.bytecodes import dvm
from androguard.core.analysis import analysis
from androguard.misc import AnalyzeAPK

target = ["/Volumes/Backup Plus/malware_samples/droid_anl_eagle_sample_13_15_2152/"]

md5_list = []

#a is androguard.core.bytecodes.apk.APK object
#d is list of androguard.core.bytecodes.dvm.DalvikVMFormat objects!
#no use of dx (quite heavy)

f = open("./res_droids/finished_decom.txt", "w")
ctr = 0
ctr2 = 0
ctr3 = 0
f2 = open("./res_droids/failed_decom.txt", "w")

for i in target:
    target_dir = os.listdir(i)
    for item in target_dir:
        

        try:
            a  = apk.APK(i+item)

        except :
            ctr2 += 1
            print("err {} {} ".format(ctr2, item))
            md5 = subprocess.check_output("openssl dgst -md5 " + "'" + i+item + "'", stderr=subprocess.STDOUT, shell=True).decode('utf-8').split("= ")[1][:-1]
            sha256 = subprocess.check_output("openssl dgst -sha256 " + "'" + i+item + "'", stderr=subprocess.STDOUT, shell=True).decode('utf-8').split("= ")[1][:-1]
            f2.write(md5 + " " + sha256 + " " + "None" + "\n")
            
            continue

        ctr+=1
        
        pkg = a.get_package()
        if pkg == None:
            pkg = "None"
        md5 = subprocess.check_output("openssl dgst -md5 " + "'" + i+item + "'", stderr=subprocess.STDOUT, shell=True).decode('utf-8').split("= ")[1][:-1]
        sha256 = subprocess.check_output("openssl dgst -sha256 " + "'" + i+item + "'", stderr=subprocess.STDOUT, shell=True).decode('utf-8').split("= ")[1][:-1]

        if md5 not in md5_list:
            md5_list.append(md5)
    
            f.write(md5 + " " + sha256 + " " + pkg + "\n")
            print("writing {} {} \n".format(ctr, item))
        else:
            print("overlapping {} {} \n".format(i, item))
            ctr3 += 1
            ctr = ctr-1

        time.sleep(0.1)

print("com vs fail vs overlap = {} : {} : {}".format(ctr, ctr2, ctr3))

f.close()
f2.close()


#a = apk.APK("./malbus/19162b063503105fdc1899f8f653b42d1ff4fcfcdf261f04467fad5f563c0270.apk")
#d = dvm.DalvikVMFormat(a.get_all_dex())

#show summary
#a.show()



#extract Androidmanifest.xml

'''
def printIntentFilters(a, itemtype, name):
    print (itemtype + ' - ' + name + ':')
    for action,intent_name in a.get_intent_filters(itemtype, name).items():
                print ('\t' + action + ':')
                for intent in intent_name:
                        print ('\t\t' + intent)
    return

def print_filters(a):
    # activity, service, receiver - intent filters
    print('Activities and their intent-filters:\n\n')
    activities = a.get_activities()
    activityString = 'activity'
    for activity in activities:
        printIntentFilters(a, activityString, activity)
    print('\nServices and their intent-filters:\n\n')
    services = a.get_services()
    serviceString = 'service'
    for service in services:
        printIntentFilters(a, serviceString, service)
    print('\nReceivers and their intent-filters:\n\n')
    receivers = a.get_receivers()
    receiverString = 'receiver'
    for receiver in receivers:
        printIntentFilters(a, receiverString, receiver)



def ext_apkinfos(a):
    pkg = a.get_package()

    ver_min = a.get_min_sdk_version()
    ver_tar = a.get_target_sdk_version()
    ver_max = a.get_max_sdk_version()

def ext_permissions(a):
    #declared & aosp's
    dec_perm = a.get_declared_permissions()
    req_perm = a.get_requested_aosp_permissions()

def ext_activities(a):
    act = a.get_activities()

def ext_services(a):
    svc = a.get_services()

def ext_receivers(a):
    rec = a.get_receivers()

def ext_providers(a):
    pvd = a.get_providers()

def ext_files(a):
    files = a.get_files()

def ext_urls(d):
    urls = []

    #Mutilple Dex files
    for di in d:
        #URL Regex = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
        urls += (di.get_regex_strings('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'))
    urls = list(set(urls))
    return urls

def dump_manifest(apk_file):
    a = apk.APK(apk_file)

#print_filters(a)

urls = ext_urls(d)
#print(len(urls))
#print(urls)

#apk method
def dump_method(apk_file):
    call_method=[]
    a = apk.APK(apk_file)
    d = dvm.DalvikVMFormat(a.get_dex())
    for current_class in d.get_classes():
        for method in current_class.get_methods():
            call_method.append(method.get_name())

    call_method = list(set(call_method))

    return call_method, len(call_method)

#apk
def dump_permissions(apk_file):
    call_permissions = []
    a = apk.APK(apk_file)
    for per in a.get_permissions():
        per=per.split(".")
        call_permissions.append(per[-1])

    call_permissions = list(set(call_permissions))

    return call_permissions, len(call_permissions)

'''