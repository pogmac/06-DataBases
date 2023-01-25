import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """ create a database connection to the SQLite database
    specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn

def execute_sql(conn, sql):
   """ Execute sql
   :param conn: Connection object
   :param sql: a SQL script
   :return:
   """
   try:
       c = conn.cursor()
       c.execute(sql)
       conn.commit()
       c.close
   except Error as e:
       print(e)

def select_task_by_status(conn, status):
   """
   Query tasks by priority
   :param conn: the Connection object
   :param status:
   :return:
   """
   cur = conn.cursor()
   cur.execute("SELECT * FROM tasks WHERE status=?", (status,))

   rows = cur.fetchall()
   return rows

conn = create_connection("database.db")
cur = conn.cursor()
cur.execute("SELECT * FROM tasks")
print(cur.execute("SELECT * FROM tasks"))

rows = cur.fetchall()
print(rows)


print()
cur.execute("SELECT * FROM tasks")
#print(cur.fetchone())

for i in range(10):
    print(cur.fetchone())

print()
print(select_task_by_status(conn,"in progress"))


def select_all(conn, table):
   """
   Query all rows in the table
   :param conn: the Connection object
   :return:
   """
   cur = conn.cursor()
   cur.execute(f"SELECT * FROM {table}")
   rows = cur.fetchall()

   return rows

print("select_all")
print(select_all(conn,"tasks"))

def select_where(conn, table, **query):
   """
   Query tasks from table with data from **query dict
   :param conn: the Connection object
   :param table: table name
   :param query: dict of attributes and values
   :return:
   """
   cur = conn.cursor()
   qs = []
   values = ()
   for k, v in query.items():
       qs.append(f"{k}=?")
       values += (v,)
   q = " AND ".join(qs)
   cur.execute(f"SELECT * FROM {table} WHERE {q}", values)
   rows = cur.fetchall()
   return rows

print("tasks")
print(select_where(conn, "tasks", project_id=2))

print("tasks in progress")
print(select_where(conn, "tasks", status="in progress"))



