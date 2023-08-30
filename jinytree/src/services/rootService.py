from collections import OrderedDict
from difflib import get_close_matches
from ..db.dictionaryDataList import word_dict

class RootService:
    @classmethod
    def matchDatas(cls,word,first_word):
        n = 3;
        cutoff = 0.8
        candidates = word_dict
        
        maches_data = get_close_matches(word, candidates, n, cutoff)

        return  maches_data
    

    