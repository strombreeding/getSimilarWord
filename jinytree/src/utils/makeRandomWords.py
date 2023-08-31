import json
import random

# s.json 파일 읽기
def generate_random_words():
    with open('dictionary.json', 'r') as json_file:
        data = json.load(json_file)
        word_dict = data.get("word", {})

    all_words = []
    for words in word_dict.values():
        all_words.extend(words)

    if len(all_words) < 50:
        raise ValueError("단어 리스트의 길이가 충분하지 않습니다.")

    # 무작위로 50개 단어 추출
    random_words = random.sample(all_words, 50)

    # 결과 출력
    result = ", ".join(random_words)
    return result