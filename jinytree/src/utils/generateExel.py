import pandas as pd


def generate_exel_file(response_data):
    data_list = []
    for key, values in response_data.items():
        row = [key] + values
        data_list.append(row)

    columns = ['검색어', '유사단어 1', '유사단어 2']  # 엑셀 파일의 컬럼명

    # 데이터 리스트를 데이터프레임으로 변환
    df = pd.DataFrame(data_list, columns=columns)

    # 데이터프레임을 엑셀 파일로 저장
    excel_file_path = 'similar_words_formatted.xlsx'
    df.to_excel(excel_file_path, index=False)

    print(f"Data saved to {excel_file_path}")