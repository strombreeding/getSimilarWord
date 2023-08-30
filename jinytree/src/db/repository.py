import json

class DictionaryDb:

    def findByFirstWord(first_word):
        print("사전 모듈 실행")
        with open("dictionary.json", 'r') as json_file:
            data = json.load(json_file)
            value = data.get('word', {}).get(first_word, None)
            return value