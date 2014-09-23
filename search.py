# encoding: utf-8
'''
Created on 2014��9��23��

@author: biao
'''

import timeit

#s = raw_input()
flag  = False

def search(s):
    i = 0
    fp = open("e-c","r")
    flag = False
    for line in fp:
        i += 1
        if line.split(":",1)[0] == s:
            flag = True;
            #print line
            break;
        if flag:
            break;
    #print "search: %s" % i
        
def binary_search(s):
    i = 0
    fp = open("e-c","r")
    words = fp.readlines()
    low = 0
    high = len(words) - 1;
    while low <= high:
        i += 1
        mid = (low + high) / 2
        word = words[mid].split(":",1)[0]
        if word == s:
            #print "binary_search: %s" % i
            return words[mid]
        if word < s:
            low = mid + 1
        else:
            high = mid - 1
    #print "binary_search: %s" % i
    return False
        


def re():
    fp = open("dictionary","r")
    fp2 = open("e-c1","w")
    words = []
    for line in fp.readlines():
        words.append(line)
    sorted(words)
    for word in words:
        fp2.write(word)
    fp.close()
    fp2.close()
    
def test1():
    s = 0
    n = 0
    fp = open("e-c","r")
    for line in fp:
        n += 1
        word = line.split(":",1)[0]
        s += timeit.timeit("search('%s')" % word, "from __main__ import search", timeit.default_timer, 1)
        print n
    print sum / n;
    
def test2():
    s = 0
    n = 0
    fp = open("e-c","r")
    for line in fp:
        n += 1
        word = line.split(":",1)[0]
        s += timeit.timeit("binary_search('%s')" % word, "from __main__ import binary_search", timeit.default_timer, 1)
    print s / n;
    

if __name__=='__main__':
    #print timeit.timeit("search('Will')", "from __main__ import search", timeit.default_timer, 1)
    #print timeit.timeit("binary_search('Will')", "from __main__ import binary_search", timeit.default_timer, 1)
    test1()
    test2()