from collections import OrderedDict
from difflib import get_close_matches
from ..db.repository import DictionaryDb

class RootService:
    @classmethod
    def matchDatas(cls,word,first_word):
        n = 3;
        cutoff = 0.55
        candidates = DictionaryDb.findByFirstWord(first_word)
        word = word.replace(" ", "")
        maches_data = list(set(get_close_matches(word, candidates, n, cutoff)))
        if len(maches_data) != 0:
            words = maches_data
            for item in words:
                if item == word:
                    maches_data.remove(word)
        
        return  maches_data
    

    