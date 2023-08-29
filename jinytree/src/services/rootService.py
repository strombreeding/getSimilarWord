from difflib import get_close_matches
from ..db.connect import Candidates
candidates = Candidates

class RootService:
    @classmethod
    def matchDatas(cls,word):
        n = 2;
        cutoff = 0.5
        maches_data = get_close_matches(word, candidates, n, cutoff)
        return  maches_data
    
        # maches_data = get_close_matches(word, candidates, n, cutoff)
        # maches_data = {item: item for item in maches_data}
        # return  maches_data
    