from fastapi import  APIRouter, Query
from ..services.rootService import RootService
import time
import os
import re
from fastapi.responses import HTMLResponse


rootRouter = APIRouter()



@rootRouter.get("/", response_class=HTMLResponse)
async def read_root():
    return "goto /getSimliarWord?wordList=hell"


def has_uppercase(text):
    pattern = r'[A-Zㄱ-힣]+'
    match = re.search(pattern, text)
    return bool(match)



@rootRouter.get("/getSimliarWord")
def get_similar_words(
    wordList:str = Query(..., description="Input word for similarity comparison"),
):
    start_time = time.time()
    wordList = wordList.split(",")
    for word in wordList:
        if has_uppercase(word):
            return "대문자 또는 한글이 포함되어있습니다."
    result = {}
    for i in range(0, len(wordList)):
        first_word = wordList[i][0]
        result[wordList[i]] = RootService.matchDatas(wordList[i],first_word)
    print("result = ",result)

    end_time = time.time()
    print("job done",end_time - start_time)
    return result