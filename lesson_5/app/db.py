import sqlite3


connection = sqlite3.connect("shop.db")
cursor = connection.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS fruits (
id INTEGER,
name VARCHAR (30),
price VARCHAR (30)
)
""")

def get_fruits():
    fruits = cursor.execute("SELECT name FROM fruits")
    fruits = cursor.fetchall()
    # print(fruits)
    list_fruits = []
    for i in fruits:
        list_fruits.append(i[0])
    # print(list_fruits)
    return list_fruits
    

get_fruits()