# import pymysql

# # DB Connection 생성
# sql = 'SELECT word from word'
# con = pymysql.connect(host='',
#                     user='root',
#                     password='',
#                     db='golf',
#                     charset='utf8') # 한글처리 (charset = 'utf8')
# cur = con.cursor()
# cur.execute(sql)
# sql_result = cur.fetchall()
# con.close()

# Candidates = []
# for i in range(0,len(sql_result)):
#     Candidates.append(sql_result[i][0])