from fastapi import  APIRouter, Query
from ..services.root import RootService
from ..utils.makeList import makeList
rootRouter = APIRouter()

@rootRouter.get("/getSimliarWord")
def get_similar_words(
    wordList:str = Query(..., description="Input word for similarity comparison"),
):
    wordList = wordList.split(",")
    print(wordList)
    candidates = ['lear', 'learn', 'lean', 'love']
    n = 4;
    cutoff = 0.6

    result = {}
    for i in range(0, len(wordList)):
        result[wordList[i]] = RootService.matchDatas(wordList[i],candidates,n,cutoff)
    return result