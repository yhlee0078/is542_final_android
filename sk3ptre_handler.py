import os
import subprocess
import os.path

#cmd = '7z x ./2FAStealer.zip -pinfected -o/Users/underdog/is542_final/sk3ptre_sample'

target = ["/Volumes/Backup Plus/AndroidMalware_2019/", '/Volumes/Backup Plus/AndroidMalware_2020/']

for i in range(len(target)):
    files = os.listdir(target[i])
    for item in files:
        if os.path.isdir(target[i] + item) == False:
            os.system("7z x " + "'" +target[i] + item + "'" + " -pinfected -o/Users/underdog/is542_final/sk3ptre_sample")
            print('Done : ' + item + '\n')
