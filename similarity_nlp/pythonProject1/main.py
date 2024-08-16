import psycopg2
import pandas as pd

conn_params = {
    "host":"localhost",
    "database":"postgres",
    "user":"postgres",
    "password":"321tiger",
}

if __name__ == "__main__":
    df = pd.read_csv("data/영화리뷰유사도데이터.csv", sep=',', on_bad_lines='skip')

    # idx = 2
    # for text,label in zip(df["text"], df["labels"]):
    #     try:
    #         insert_query = f'''insert into review values ({idx}, '{text}', {label});'''
    #         idx +=1
    #         connect = psycopg2.connect(**conn_params)
    #         cursor = connect.cursor()
    #         cursor.execute(insert_query)
    #         connect.commit()
    #     except Exception as e:
    #         print(e)
    #     else:
    #         if connect:
    #             cursor.close()
    #             connect.close()
    #         print('Success')


    my_input = input("검색어 입력 : ")
    try:
        test_query =f'''
        select text, similarity(lower('{my_input}'), lower(text)) as similarity_score  from review order by similarity_score desc limit 10;'''
        connect = psycopg2.connect(**conn_params)
        cursor = connect.cursor()
        cursor.execute(test_query)
        results = cursor.fetchall()
        connect.commit()
    except Exception as ex :
        print(ex)
    else:
        for result in results:
            print(result[0][:20] , ' 정확도 : ' , round(float(result[1]) * 100,2), "%")
        if connect:
            cursor.close()
            connect.close()

