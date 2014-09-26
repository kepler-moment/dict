# encoding: utf-8
'''
Created on 2014/9/23

@author: kepler-moment
'''

from dictionary import Dictionary
    
def getDictMap(path):
    fp = open(path,"r")
    words = {}
    for line in fp.readlines():
        word = line.split(":",1)
        words[word[0]] = word[1]
        #print word[0]
    return words


if __name__=='__main__':
    #print timeit.timeit("search('Will')", "from __main__ import search", timeit.default_timer, 1)
    #print timeit.timeit("binary_search('Will')", "from __main__ import binary_search", timeit.default_timer, 1)
    dictionary = Dictionary(getDictMap("./e-c"))
    while True:
        word = raw_input()
        v = dictionary.search(word)
        if len(v) == 0:
            print dictionary.getSimilarWord(word)
        else:
            print v
    