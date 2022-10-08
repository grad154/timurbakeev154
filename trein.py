sel=int(input("МЕНЮ 1.Создание и ввод даннных БД 2.SQL-запрос"))
if sel==1:
  create()
elif sel==2:
  sq=input("SQL-запрос:")
  sql(sq)
