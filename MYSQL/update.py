

import pymysql


my_db = pymysql.connect(

        host="localhost",

        user="root",

        password="chsasake2007",
        
        database="TEST_DB"
)

my_cursor = my_db.cursor()

def insert_concert_from_user_input():
    datum = input("Datum: ")
    land = input("Land: ")
    stadt = input("Stadt: ")

    val = f'"{datum}", "{land}", "{stadt}"'
    sql = f'INSERT INTO konzerte VALUES ({val})'

    my_cursor.execute(sql)
    my_db.commit()

def show_all_data():
    my_cursor.execute("SELECT * FROM konzerte")
    result = my_cursor.fetchall()
    for _ in result:
        print(_)

def update_city():
    old_city = input('Welche Stadt soll ersetzt werden? ' )
    new_city = input('Welche Stadt soll stattdessen eingetragen werden? ')

    sql = f"UPDATE konzerte SET stadt = '{new_city}' WHERE stadt = '{old_city}'"

    sql = f"UPDATE konzerte SET stadt = '{new_city}' WHERE stadt = '{old_city}'"
    
    my_cursor.execute(sql)
    my_db.commit()
update_city()
show_all_data()
