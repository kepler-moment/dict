'''
Created on 2014/9/26

@author: kepler-moment
'''
  
class Trie:
    """Trie tree"""
    
    class Node:
        """Used as node of Trie"""
        
        def __init__(self,numofchar):
            self._isWord = False        #whether the node is the end of a word
            self.NUMOFCHAR = numofchar  #number of children
            self.value = None           #key word of node
            self.next = [None] * self.NUMOFCHAR
        
        def setWord(self,value):
            self._isWord = True
            self.value = value
            
        def isWord(self):
            return self._isWord
        
        def getValue(self):
            return self.value
    
    
    NUMOFLOW = 26
    def __init__(self,dict_map):
        #root of word which is converted to lower
        self.rootOfLow = self.Node(26)
        #root of work which has capical
        self.rootOfCapital = self.Node(self.NUMOFLOW * 2)
        for (key,value) in dict_map.items():
            self.insert(key,value)
      
    def hasCapital(self,key):
        """check whether key has capitals"""
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
                    newNode = self.Node(self.NUMOFLOW * 2)
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
                    newNode = self.Node(self.NUMOFLOW)
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
        if root != None and root.isWord() is True and i == len(key):
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
            if root != None and root.isWord() is True and i == len(key):
                d[key] = root.getValue()
        return d
