import os
import csv
import settings
count = 0

with open('software.csv', 'w', newline='') as f:
    writer = csv.writer(f)

    softsource = settings.share_root
    soft_list = os.listdir(softsource)

    for dirs in soft_list:
    #print(dirs)
        soft_dir = os.path.join(softsource, dirs)
        versions = os.listdir(soft_dir)
        for version in versions:
            #print(dirs+version)
            soft_version = os.path.join(soft_dir, version)
            #print(soft_version)
            if os.path.isdir(soft_version):
                ini_files = os.listdir(soft_version)
                #print(soft_version)
            for ini in ini_files:
                if ini.endswith(".ini") and ini.startswith(dirs):
                    count += 1
                    #print(dirs+version+ini)
                    writer.writerow([count,dirs,version,ini])
                
                
                    
            
        
