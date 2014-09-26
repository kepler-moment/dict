# encoding: utf-8
'''
Created on 2014/9/25

@author: kepler-moment
'''

from editDistance import editDistance

class BK_Tree:
    """"""
    
    class Node:
        """data structure of BK_Tree's nodes"""
        
        #initial number of children
        __NUMOFCHILDREN = 20
        def __init__(self,word = None):
            self.word = word
            self.children = [None] * self.__NUMOFCHILDREN;
        
        def resizeChildren(self,newSize):
            """resize the number of children"""
            assert newSize > len(self.children)
            self.children += [None] * (newSize - len(self.children))
        
        def getNumOfChildren(self):
            return len(self.children)   
           
    def __init__(self):
        self.root = None
        
    def insert(self,word):
        #print word
        if self.root is None:
            self.root = self.Node(word)
            return 
        r = self.root
        while True:
            distance = editDistance(r.word, word)
            if distance > r.getNumOfChildren():
                r.resizeChildren(distance)
            if r.children[distance] is None:
                r.children[distance] = self.Node(word)
                return
            r = r.children[distance]
    
    def __search(self,word,root,maxDistance):
        if root is None:
            return None
        s = {}
        distance = editDistance(root.word,word)
        if distance <= maxDistance:
            s[root.word] = distance
        l = max(0,distance - maxDistance)
        r = min(len(root.children),distance + maxDistance + 1)
        #print "len: %s" % len(root.children)
        #print "dis: %s" % distance
        #print "word: %s" % root.word
        for i in range(l,r):
            #print i
            if root.children[i] is not None:
                tmp = self.__search(word,root.children[i],maxDistance)
                if tmp is not None:
                    s.update(tmp.items())
        return s
        
    def topKSimilar(self,word,k = 5,maxDistance = 5):
        """get top k similar words"""
        r = self.__search(word,self.root,maxDistance)
        return sorted(r.items(),key = lambda x:x[1])[0:k]
                