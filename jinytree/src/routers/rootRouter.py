from fastapi import  APIRouter, Query
from ..services.rootService import RootService
import time
import os
from fastapi.responses import HTMLResponse


rootRouter = APIRouter()



@rootRouter.get("/", response_class=HTMLResponse)
async def read_root():
    return "goto /getSimliarWord?wordList=hell"



@rootRouter.get("/getSimliarWord")
def get_similar_words(
    wordList:str = Query(..., description="Input word for similarity comparison"),
):
    start_time = time.time()
    wordList = wordList.split(",")
    if wordList[0] == wordList[0].upper():
        return "대문자 또는 한글을 빼주세요."
    result = {}
    for i in range(0, len(wordList)):
        first_word = wordList[i][0]
        result[wordList[i]] = RootService.matchDatas(wordList[i],first_word)
    print("result = ",result)

    end_time = time.time()
    print("job done",end_time - start_time)
    return result