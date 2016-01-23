'''
Created on 13.01.2016

@author: Admin
'''

import bisect
import statistics
import os
import timeit
from timeit import Timer


def lcountEarly(filelist):
    topz = []
    fails = []
    
    for x in range(len(filelist)):
        zeilen = 0
        try:
            for l in open(filelist[x]).readlines():
                if len(l.strip()) > 0:
                    zeilen +=1
            bisect.insort_left(topz, [zeilen,filelist[x]])
        except:
            fails.append([-1,filelist[x]])
            pass
    return [topz,fails]
    
def lcountLate(filelist):
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

    
def findFiles(filetype, meth):
    filelist = []
    for path,_folders,files in os.walk('.'):
        for file in files:
            if file.endswith(filetype):
                filelist.append(os.path.join(path, file))
    
    if meth == "lcountEarly":
        re = lcountEarly(filelist)
    if meth == "lcountLate":
        re = lcountLate(filelist)
    #if method == "dcountEarly":
    #    re = lcountEarly(filelist)
    #if method == "dcountLate":
    #    re = lcountEarly(filelist)
    #printStats(re[0],re[1])
    
    
def luki(lol):
    return "loool"
    
    
def printStats(topz,fails):
    
    print(len(topz),"READABLE files found!")
    print(len(fails),"UNREADABLE files found!")
    print(round(statistics.mean([x[0] for x in topz]),2),"lines is avg!")
    print(statistics.median([x[0] for x in topz]),"lines is median")
    print()
    if len(topz) > 2:
        print("--- Start Top3 ---")
        print("Linecount - Filename")
        for x in range(1,4):
            print(topz[len(topz)-x][0],"  -  ",topz[len(topz)-x][1])
        print("--- Stop Top3 ---")
        print()
        print("--- Start Low3 ---")
        print("Linecount - Filename")
        for x in range(3):
            print(topz[x][0],"  -  ",topz[x][1])
        print("--- Stop Low3 ---")
    else:
        print("Not enough data for top3/low3 :(")
    
#findFiles((""),"lcountEarly")
#findFiles((""),"lcountLate")
e = Timer(lambda: findFiles((""),"lcountEarly"))
l = Timer(lambda: findFiles((""),"lcountLate"))
findFiles((""),"lcountEarly")
findFiles((""),"lcountLate")
#
early = (e.timeit(number=100))
late = (l.timeit(number=100))
print("Early: ",early)
print("Late: ",late)


