#!/usr/bin/env python
import random
import time
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot

def i_sort(nthings):
    lista = []
    lista = [random.randint(0,1000) for r in xrange(nthings)]
    for x in range(1, len(lista)):
        number = lista[x]
        y = x - 1
        while (y >= 0) and (lista[y] > number):
            lista[y + 1] = lista[y]
            y = y - 1
        lista[y + 1] = number
        
def m_sort(mthings):
    listb = []
    listb = [random.randint(0,1000) for r in xrange(mthings)]
    if len(listb) <= 1:
        return listb
    
    splitter = len(listb)/2
    list1 = listb[:splitter]
    list2 = listb[splitter:]
    list1 = m_sort(list1)
    list2 = m_sort(list2)
    final = []
    while len(list1) > 0 and len(list2) > 0:
        if list1[0] > list2[0]:
            final.append(list2.pop(0))
        else:
            result.append(list1.pop(0))
    if len(list1) > 0:
        final.extend(m_sort(list1))
    else:
        final.extend(m_sort(list2(0)))
    
    
        
        
#def merge_sort(listb):

def getRunningTime(func, maxN=250, repetitions=100):
	times = []

	for n in range(1, maxN):
		start = time.clock()
		for rep in range(repetitions):
			func(n)
		end = time.clock()
		avg = (end-start)/float(repetitions)
		times.append(avg)

	return times 

def getRunningTime2(func, maxN=250, repetitions=100): #can give two imputs to this function important for doing the the homework
	times = []

	for n in range(1, maxN):
		start = time.clock()
		for rep in range(repetitions):
			func(n-1, n)
		end = time.clock()
		avg = (end-start)/float(repetitions)
		times.append(avg)

	return times 


def plotRunningTime(times, name="plot"): 
	x = range(len(times))
	pyplot.plot(x, times, 'o')
	pyplot.savefig(name + "%d.png" % len(times))
	pyplot.close()

'''       
insertion_time = getRunningTime(i_sort, 100000, 100)
plotRunningTime(insertion_time, "Insertion Sort")
'''
insertion_time = []
insertion_time = getRunningTime2(i_sort, m_sort, 100, 100)
print insertion_time
plotRunningTime(insertion_time, "Insertion Time")
'''
merge_time = []
merge_time = getRunningTime2(m_sort, 100, 100)
print merge_time
plotRunningTime(merge_time, "Merge Sort")
'''