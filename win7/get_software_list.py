import os
import csv
count = 0

with open('software.csv', 'w', newline='') as f:
    writer = csv.writer(f)

    softsource = r"\\frk-fna-fs01\support\software"
    soft_list = os.listdir(softsource)

    for dirs in soft_list:
    #print(dirs)
        soft_dir = os.path.join(softsource, dirs)
        versions = os.listdir(soft_dir)
        for version in versions:
        #print(dirs+","version)
            soft_version = os.path.join(soft_dir, version)
            if os.path.isdir(soft_version):
                ini_files = os.listdir(soft_version)
            for ini in ini_files:
                if ini.endswith(".ini") and ini.startswith(dirs):
                    count += 1
                    writer.writerow([count,dirs,version,ini])
                
                
                    
            
        
