import sqlite3
from sqlite3 import Error

def create_connection(db_file):
   """ create a database connection to the SQLite database
       specified by the db_file
   :param db_file: database file
   :return: Connection object or None
   """
   conn = None
   try:
       conn = sqlite3.connect(db_file)
   except Error as e:
       print(e)

   return conn

def update(conn, table, id, **kwargs):
   """
   update status, begin_date, and end date of a task
   :param conn:
   :param table: table name
   :param id: row id
   :return:
   """
   parameters = [f"{k} = ?" for k in kwargs]
   parameters = ", ".join(parameters)
   print(parameters)
   values = tuple(v for v in kwargs.values())
   print(values)
   values += (id, )
   print(values)

   sql = f''' UPDATE {table}
             SET {parameters}
             WHERE id = ?'''

   print(sql)             
   try:
       cur = conn.cursor()
       cur.execute(sql, values)
       conn.commit()
       print("OK")
   except sqlite3.OperationalError as e:
       print(e)


#if __name__ == "__main__":
#conn = create_connection("database.db")
#update(conn, "tasks", 6, status="new status")
#update(conn, "tasks", 2, stat="started")
#conn.close()



### DELETE BEGIN ###
#DELETE FROM tasks WHERE id=3

def delete(conn, table, id):

    sql = f'''DELETE FROM {table}
            WHERE ID = {id}'''
    print(sql)             
    try:
       cur = conn.cursor()
       cur.execute(sql)
       conn.commit()
       print("OKEY")
    except sqlite3.OperationalError as e:
       print(e)

#if __name__ == "__main__":
#   conn = create_connection("database.db")
#   delete(conn, "tasks", 2)
#   conn.close()

#conn = create_connection("database.db")
#delete(conn, "tasks", 8)
#conn.close()

def delete_where(conn, table, **kwargs):
   """
   Delete from table where attributes from
   :param conn:  Connection to the SQLite database
   :param table: table name
   :param kwargs: dict of attributes and values
   :return:
   """
   qs = []
   values = tuple()
   for k, v in kwargs.items():
       qs.append(f"{k}=?")
       values += (v,)
       print(v,k,qs,values)
   q = " AND ".join(qs)
   print(q)
   sql = f'DELETE FROM {table} WHERE {q}'
   cur = conn.cursor()
   cur.execute(sql, values)
   conn.commit()
   print("Deleted")

#conn = create_connection("database.db")
#delete_where(conn, "tasks", id = 8, project_id =3)
#conn.close()


def delete_all(conn, table):
   """
   Delete all rows from table
   :param conn: Connection to the SQLite database
   :param table: table name
   :return:
   """
   sql = f'DELETE FROM {table}'
   cur = conn.cursor()
   cur.execute(sql)
   conn.commit()
   print("Deleted")


#conn = create_connection("database.db")
#delete_all(conn, "students")
#conn.close()


### DELETE END ###

### DROP BEGIN ###

import sqlite3
from sqlite3 import Error

conn = sqlite3.connect("database.db")

c = conn.cursor()
c.execute('DROP TABLE students')

conn.commit()
c.close
conn.close()

### DROP END ###

"""
conn = sqlite3.connect("database.db")
c = conn.cursor()

c.execute('DELETE FROM tasks WHERE id=3')

conn.commit()
c.close
conn.close()
"""