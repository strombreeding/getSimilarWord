h1 영단어 검색시 유사한 값 3개를 리턴 받는 프로젝트 입니다.

h2 파이썬이 설치되어 있다고 가정하고, 실행하는 법은 다음과 같습니다.

h3 pip install -r requirements.txt
h3 uvicorn src.main:app --host 0.0.0.0 --port 8000

h3 요청 : GET- URL/get_similar_words?wordList=[word1, word2]

h4 리턴값
{
"word1": [
"similarWord1",
"similarWord2",
"similarWord3"
],
"word1": [
"similarWord1",
"similarWord2"
],
}

Provider of English word dictionary
Copyright © J Ross Beresford 1993-1999
영어 단어 사전 제공자는 Ross Beresford 씨 입니다.
영단어 데이터 사용시 꼭 카피라이트를 적어주시길 바래요.

-- 추후 한국어 단어 검색도 추가

--업데이트노트
0 영단어 유사 단어 추출기 API서버
