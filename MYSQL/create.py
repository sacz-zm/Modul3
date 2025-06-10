

#################################################################################
# Durch Probleme mit dem MySQL-Connector, musste auf pymysql umgestiegen werden
#################################################################################
import pymysql


my_db = pymysql.connect(

        host="localhost",

        user="root",

        password="chsasake2007"
)

my_cursor = my_db.cursor()
my_cursor.execute("CREATE DATABASE TEST_DB")
my_cursor.execute("SHOW DATABASES")
for db in my_cursor:
    print(db)