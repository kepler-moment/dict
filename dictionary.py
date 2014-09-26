'''
Created on 2014/9/26

@author: kepler-moment
'''

from Trie import Trie
from BK_Tree import BK_Tree
from editDistance import editDistance

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
        return self.similar_tree.topKSimilar(word, num, maxDistance)

    def editDistanceTopK(self,key,k,distance):
        
        def cmp1(word1,word2):
            """"sort similarWord by distance"""
            if word1['distance'] < word2['distance']:
                return -1
            return 1
    
        assert k >= 1
        assert distance >= 0
        similarWord = []
        for (kt,va) in self.dict_map.items():
            d = editDistance(key,kt)
            if d <= distance:
                similarWord.append({})
                similarWord[len(similarWord) - 1] = {kt:va,"distance":d};
        similarWord.sort(cmp1)
        return similarWord[0:k]