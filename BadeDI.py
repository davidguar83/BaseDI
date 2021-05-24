import sqlite3 as dbapi

try:
    bbdd = dbapi.connect ("baseDI.dat")
    print (bbdd)


except dbapi.StandardError as e:
    print (e)
else:
    print ("Base de datos aberta")

try:
    cursor = bbdd.cursor ()
    print (cursor)

except dbapi.Error as e:
    print (e)
else:
    print ("Cursor preparado")



try:


    cursor.execute("""CREATE TABLE clientes (
    "DNI"	TEXT PRIMARY KEY NOT NULL,
    "nome"	TEXT NOT NULL,
    "apelledos"	TEXT NOT NULL,
    "telf"	INTEGER NOT NULL,
    "deuda"	INTEGER NOT NULL
    )
    """)

    bbdd.commit()

    cursor.execute("""insert into clientes
                     values ( '53177986p', 'David', 'rodriguez',986123456,150)""")


    cursor.execute("""insert into clientes
                     values ( '53177988x', 'Jose', 'rodriguez',986654321,1000)""")

    bbdd.commit()


except dbapi.DatabaseError as e:
    print("Erro insertando os datos en clientes: " + str(e))



try:

    cursor.execute("""CREATE TABLE productos (
    "ref"	INTEGER PRIMARY KEY NOT NULL,
    "nome"	TEXT NOT NULL,
    "pvp"	INTEGER NOT NULL
    )
    """)

    bbdd.commit()




    cursor.execute("""insert into clientes
                     values ( 1, 'patata', 0.25)""")

    cursor.execute("""insert into clientes
                     values ( 2, 'melon', 2.35)""")
    cursor.execute("""insert into clientes
                     values ( 3, 'nocilla', 3.25)""")
    cursor.execute("""insert into clientes
                     values ( 4, 'lentejas', 0.80)""")


    bbdd.commit()


except dbapi.DatabaseError as e:
    print("Erro insertando os datos en clientes: " + str(e))

try:

    cursor.execute("""CREATE TABLE ventas (
    "ref"	INTEGER PRIMARY KEY NOT NULL,
    "nome"	TEXT NOT NULL,
    "cantidad"	INTEGER NOT NULL
    )
    """)


    bbdd.commit()




    cursor.execute("""insert into clientes
                     values ( 1, 'patata', 150)""")
    cursor.execute("""insert into clientes
                     values ( 2, 'melon', 150)""")
    cursor.execute("""insert into clientes
                     values ( 3, 'nocilla', 150)""")
    cursor.execute("""insert into clientes
                     values ( 4, 'lentejas', 150)""")


    bbdd.commit()




except dbapi.DatabaseError as e:
    print("Erro insertando os datos en clientes: " + str(e))
