# encoding: utf-8
'''
Created on 2014/9/23

@author: kepler-moment
'''

class Node:
    """Used as node of Trie"""
    
    def __init__(self,numofchar):
        self._isWord = False
        self.NUMOFCHAR = numofchar
        self.value = None
        self.next = [None] * self.NUMOFCHAR
    
    def setWord(self,value):
        self._isWord = True
        self.value = value
        
    def isWord(self):
        return self._isWord
    
    def getValue(self):
        return self.value

   
class Trie:
    """Trie tree"""
    NUMOFLOW = 26
    def __init__(self,dict_map):
        #the root of word which is converted to lower
        self.rootOfLow = Node(26)
        #the root of work which has capical
        self.rootOfCapital = Node(self.NUMOFLOW * 2)
        for (key,value) in dict_map.items():
            self.insert(key,value)
      
    def hasCapital(self,key):
        for i in range(len(key)):
            if key[i].isupper():
                return True
        return False   
        
    def insert(self,key,value):
        """insert key => value"""
        lenOfkey = len(key)
        
        """if there is capital in key,insert it into rootOfCapital"""

        if self.hasCapital(key):
            root = self.rootOfCapital
            for i in range(lenOfkey):
                if key[i].isupper():
                    tmp = ord(key[i]) - ord('A') + self.NUMOFLOW
                else:
                    tmp = ord(key[i]) - ord('a')
                #print "hasC %s " % key
                if root.next[tmp] is None:
                    newNode = Node(self.NUMOFLOW * 2)
                    root.next[tmp] = newNode
                root = root.next[tmp]
            root.setWord(value)
        else:
            lower_word = key.lower()
            root = self.rootOfLow
            for i in range(lenOfkey):
                tmp = ord(lower_word[i]) - ord('a')
                #print tmp
                #print lower_word
                if root.next[tmp] == None:
                    newNode = Node(self.NUMOFLOW)
                    root.next[tmp] = newNode
                root = root.next[tmp]
            root.setWord(value)
                    
    def search(self,key):  
        d = {}
        low_word = key.lower()
        root = self.rootOfLow
        for i in range(len(key)):
            tmp = ord(low_word[i]) - ord('a')
            if root.next[tmp] is None:
                break
            root = root.next[tmp]
        if root != None and root.isWord() is True:
            d[low_word] = root.getValue()
        if self.hasCapital(key):
            root = self.rootOfCapital
            for i in range(len(key)):
                if key[i].isupper():
                    tmp = ord(key[i]) - ord('A') + self.NUMOFLOW
                else:
                    tmp = ord(key[i]) - ord('a')
                if root.next[tmp] is None:
                    break
                root = root.next[tmp]
            if root != None and root.isWord() is True:
                d[key] = root.getValue()
        return d        
        
class Dictionary:
    """"""
    def __init__(self,dict_map):
        """
        param dict_map is a map of all words which likes
        dict_map['english'] = 'chinese' 
        """
        self.dictionary = Trie(dict_map)
    
    def search(self,key):
        """search word in dict"""
        return self.dictionary.search(key)
    
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
    print dictionary.search("A")
    print dictionary.search("zero")