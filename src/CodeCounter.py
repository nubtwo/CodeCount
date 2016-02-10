'''
Created on 13.01.2016

@author: Admin
'''

import statistics
import os
    
def countLines(filelist):
    topz = []
    fails = []
    for x in range(len(filelist)):
        zeilen = 0
        try:
            for l in open(filelist[x]).readlines():
                if len(l.strip()) > 0:
                    zeilen +=1
            topz.append([zeilen,filelist[x]])
        except:
            fails.append([-1,filelist[x]])
            pass
    return([sorted(topz, key=lambda x: x[0]),fails])

def findFiles(filetype,minbytes):
    filelist = []
    for path,_folders,files in os.walk('.'):
        for file in files:
            if file.endswith(filetype) and os.path.getsize(os.path.join(path, file)) >= minbytes:
                filelist.append(os.path.join(path, file))
    gehtbesser = countLines(filelist)
    printStats(gehtbesser[0], gehtbesser[1])
    
def printStats(topz,fails):
    print(len(topz),"READABLE files found!")
    print(len(fails),"UNREADABLE files found!")
    print(round(statistics.mean([x[0] for x in topz]),2),"lines is avg!")
    print(statistics.median([x[0] for x in topz]),"lines is median")
    print()
    if len(topz) > 2:
        print("--- Start Top5 ---")
        print("Linecount - Filename")
        for x in range(1,6):
            print(topz[len(topz)-x][0],"  -  ",topz[len(topz)-x][1])
        print("--- Stop Top5 ---")
        print()
        print("--- Start Low5 ---")
        print("Linecount - Filename")
        for x in range(5):
            print(topz[x][0],"  -  ",topz[x][1])
        print("--- Stop Low5 ---")
    else:
        print("Not enough data for top3/low3 :(")
    
findFiles("",1000)


