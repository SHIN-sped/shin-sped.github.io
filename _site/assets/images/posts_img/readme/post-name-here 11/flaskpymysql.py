from flask import Flask, jsonify
import pymysql

app = Flask(__name__)

# MySQL 연결 정보
host = 'localhost'
user = 'root'
password = 'root'
database = 'music'

@app.route('/')
def get_data_from_mysql():
    try:
        # MySQL 연결
        connection = pymysql.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )

        # 커서 생성
        cursor = connection.cursor()

        # SQL 쿼리 실행
        sql_query = "SHOW TABLES" # SELECT * FROM album
        cursor.execute(sql_query)

        # 결과 가져오기
        data = cursor.fetchall()

        # 연결과 커서 닫기
        cursor.close()
        connection.close()

        # 결과를 JSON 형태로 반환
        return jsonify(data)

    except Exception as e:
        return f"Error: {e}"

if __name__ == '__main__':
    app.run()