import os
import subprocess
import os.path

hash_list = []
fex_list = ["Zip", "Java"]

target = "/Users/underdog/is542_final/sk3ptre_sample/"


files = os.listdir(target)
for item in files:
    test = target + item
    if os.path.isdir(test) == True: # Dir
        files0 = os.listdir(test)
        for item0 in files0:
            res = subprocess.check_output("file " + test + '/' + item0 , stderr=subprocess.STDOUT, shell=True)
            res = res.decode('utf-8')
            if ("Zip" not in res) & ("Java" not in res):
                os.system("mv " + test + '/' + item0 + " /Users/underdog/is542_final/sk3ptre_sample_not_apk/")
                #print("shit " + test+'/'+item0 + "  " + res)
            else:
                os.system("mv " + test + '/' + item0 + " /Users/underdog/is542_final/sk3ptre_sample")
            
    else: # File
        res = subprocess.check_output("file " + test , stderr=subprocess.STDOUT, shell=True)
        res = res.decode('utf-8')
        if ("Zip" not in res) & ("Java" not in res):
            os.system("mv " + test + " /Users/underdog/is542_final/sk3ptre_sample_not_apk/")
            #print("shit " + test + "  " + res)
        else:
            continue
            