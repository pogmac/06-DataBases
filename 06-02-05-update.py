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
conn = create_connection("database.db")
update(conn, "tasks", 2, status="new status")
#update(conn, "tasks", 2, stat="started")
conn.close()




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


### DELETE ###

"""
conn = sqlite3.connect("database.db")
c = conn.cursor()

c.execute('DELETE FROM tasks WHERE id=3')

conn.commit()
c.close
conn.close()
"""