import pymysql

db = pymysql.connect(host='124.160.117.199', port=3306,
                     user='root', password='Meprint2020-test')
cursorc = db.cursor()
delete_sql = "DELETE FROM design_test.userextend where phoneNumber = '15890092379'"
cursorc.execute(delete_sql)
db.commit()
db.close()
cursorc.close()