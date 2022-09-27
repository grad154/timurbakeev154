import sqlite3

db = sqlite3.connect('grad.db')

# create cursor
c = db.cursor()

# c.execute("""CREATE TABLE articles (
#     title text,
#     full_text text,
#     views integer,
#     avtor text   
# )""")

#Добавление данных
c.execute("INSERT INTO articles VALUES ('Amazon is cool!', 'Amazon is really cool', 400, 'BORUM' )")

#Удаление данных
c.execute("DELETE FROM articles WHERE rowid = 2")

# Update

c.execute("UPDATE articles SET avtor = 'Admin' WHERE title = 'Amazon is cool!'")

#Выборка данных
# c.execute("SELECT * FROM articles") # * - выбор всех данных таблицы
#c.execute("SELECT title,full_text FROM  articles")


# Условия выбора 
#c.execute("SELECT rowid, * FROM articles WHERE rowid <> 5 ORDER BY views DESC") # скрытый параметр rowid
c.execute("SELECT rowid, * FROM articles")
#ORDER ЭТО СОРТИРОВКА 'DESK' - по уменьшению, пустое по возрастанию

items = (c.fetchall())
#print(c.fetchmany(1))
# print(c.fetchone()[1])

# for el in items:
#     print(el[1] + '\n' + el[4])
for el in items:
    print(el)

db.commit()

db.close()