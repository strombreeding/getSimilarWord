from difflib import get_close_matches

class RootService:
    @classmethod
    def matchDatas(cls,word,candidates,n,cutoff):
        print("들어옴")
        maches_data = get_close_matches(word, candidates, n, cutoff)
        return  set(maches_data)
    