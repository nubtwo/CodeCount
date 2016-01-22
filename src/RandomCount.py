'''
Created on 20.01.2016

@author: nubtwo
'''
import random
import bisect
from timeit import Timer

def lcountEarly():
    liste = []
    for x in range(1000):
        bisect.insort_left(liste,(random.sample(range(1000),2)))

def lcountLate():
    liste = []
    for x in range(1000):
        liste.append(random.sample(range(1000),2))
    liste.sort(key=lambda x: x[0])

lcountLate()

e = Timer(lambda: lcountLate)
l = Timer(lambda: lcountEarly)

early = (e.timeit(number=50000000))
late = (l.timeit(number=50000000))
print("Early: ",early)
print("Late: ",late)