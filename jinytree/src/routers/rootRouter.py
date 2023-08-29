from fastapi import  APIRouter, Query
from ..services.rootService import RootService
from ..utils.makeList import makeList


rootRouter = APIRouter()

@rootRouter.get("/getSimliarWord")
def get_similar_words(
    wordList:str = Query(..., description="Input word for similarity comparison"),
):
    wordList = wordList.split(",")
    # def create_dict(word):
    #     return_dict = {}
    #     return_dict[word] = RootService.matchDatas(word)
    #     return return_dict


    result = {}
    for i in range(0, len(wordList)):
        print(wordList[i])
        result[wordList[i]] = RootService.matchDatas(wordList[i])
    print("result = ",result)
    return result