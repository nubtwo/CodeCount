'''
Created on 13.01.2016

@author: Admin
'''

import statistics
import os
    
def countLines(filelist):
    for x in filelist:
        zeilen = 0
        try:
            for l in open(x).readlines():
                if len(l.strip()) > 0:
                    zeilen += 1
            filelist.update({x:{'linecount':zeilen,'valid':True}})
            #siehe unten, sonst verliert er valid:True pair
        except:
            filelist.update({x:{'linecount':-1,'valid':False}})
            pass
    return(filelist)
            
def findFiles(filetype,minbytes):
    filelist = {}
    for path,_folders,files in os.walk('.'):
        for file in files:
            if file.endswith(filetype) and os.path.getsize(os.path.join(path, file)) >= minbytes:
                filelist.update({os.path.join(path, file):{'valid':True}})
                '''
                sinnlos, weil die kommenden .update den Inhalt des unterliegenden Dicts loescht und neu setzt...
                anstelle zu "updaten" ....
                '''
                
    printStats(countLines(filelist))
        
def printStats(filelist):
    print(len([x for x in filelist if filelist[x]['valid']]),"READABLE files found!")
    print(len([x for x in filelist if not filelist[x]['valid']]),"UNREADABLE files found!")
    print(round(statistics.mean(filelist[x]['linecount'] for x in filelist if filelist[x]['valid']),2),"lines is avg!")
    print(statistics.median(filelist[x]['linecount'] for x in filelist if filelist[x]['valid']),"lines is median")
    print()
    if len([x for x in filelist if filelist[x]['valid']]) > 2:
        print("--- Start Top5 ---")
        print("Linecount - Filename")
        line_count = lambda key: filelist[key]['linecount']
        for i in [i for i in sorted(filelist,key=line_count) if filelist[i]['valid']][-5:][::-1]: #what
            print(filelist[i]['linecount'],' - ',i)
        print("--- Stop Top5 ---")
        print()
        print("--- Start Low5 ---")
        print("Linecount - Filename")
        for i in [i for i in sorted(filelist,key=line_count) if filelist[i]['valid']][:5]:
            print(filelist[i]['linecount'],' - ',i)
        print("--- Stop Low5 ---")
        print('Psychojohnny531')

findFiles("",1000)


