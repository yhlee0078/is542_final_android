import os
import subprocess
import os.path

#cmd = '7z x ./2FAStealer.zip -pinfected -o/Users/underdog/is542_final/sk3ptre_sample'

target = "/Volumes/Backup Plus/droidanalytics/"

dirs = os.listdir(target)
for item in dirs:
    if os.path.isdir(target + item) == True:
        test = os.listdir(target+item)
        for apk in test:
            if apk.endswith('.apk') == True:
                os.system("mv " + "'"+ target+item +'/' + apk +"'" + " '" + "/Volumes/Backup Plus/malware_samples/droid_anl_eagle_sample/" + "'")
                print('Done : ' + target+item+'/' +apk + '\n')

'''
dirs = os.listdir(target)
for item in dirs:
    if os.path.isdir(target + item) == False:
        if item.endswith('.apk') == True:
            os.system("mv " + "'"+ target + item + "'" + " '" + "/Volumes/Backup Plus/malware_samples/ashishb_sample/" + "'")
            print('Done : ' + target+item + '\n')
'''