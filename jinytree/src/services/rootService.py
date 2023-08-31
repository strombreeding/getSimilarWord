from collections import OrderedDict
from difflib import get_close_matches
from ..db.repository import DictionaryDb

class RootService:
    @classmethod
    def matchDatas(cls,word,first_word):
        n = 3;
        cutoff = 0.8
        candidates = DictionaryDb.findByFirstWord(first_word)
        maches_data = list(set(get_close_matches(word, candidates, n, cutoff)))
        maches_data.remove(word)
        return  maches_data
    

    