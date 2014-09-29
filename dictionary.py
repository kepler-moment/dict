'''
Created on 2014/9/26

@author: kepler-moment
'''

from Trie import Trie
from BK_Tree import BK_Tree

class Dictionary:
    """"""
    def __init__(self,dict_map):
        """
        param dict_map is a map of all words which likes
        dict_map['english'] = 'chinese' 
        """
        self.dict_trie = Trie(dict_map)
        self.similar_tree = BK_Tree()
        for key in dict_map:
            self.similar_tree.insert(key)
        self.dict_map = dict_map;
    
    def search(self,key):
        """main word in dict"""
        return self.dict_trie.search(key)
    
    def getSimilarWord(self,word,num = 5,maxDistance = 5):
        assert word is not None
        words = self.similar_tree.topKSimilar(word, num, maxDistance)
        trans = []
        for value in words:
            tmp = self.dict_trie.search(value[0])
            data = {"word": value[0],"translation":tmp[value[0]],"distance":value[1]}
            trans.append(data)
        return trans