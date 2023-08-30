
import json

# 각 알파벳 파일에서 단어들을 읽어와 리스트에 저장
word_dict = []  # 알파벳을 키로, 해당 알파벳의 단어 리스트를 값으로 가지는 사전

for letter in range(ord('a'), ord('z')+1):
    letter_word_list = []
    file_path = f'./dictionary/{chr(letter)}.txt'
    
    with open(file_path, 'r') as txt_file:
        for line in txt_file:
            word = line.strip()  # 줄 바꿈 문자 제거
            letter_word_list.append(word)
    
    # word_dict = letter_word_list
    word_dict = [*word_dict,*letter_word_list]
