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

def add_project(conn, project):
   """
   Create a new project into the projects table
   :param conn:
   :param project:
   :return: project id
   """
   sql = '''INSERT INTO projects(nazwa, start_date, end_date)
             VALUES(?,?,?)'''
   cur = conn.cursor()
   cur.execute(sql, project)
   conn.commit()
   return cur.lastrowid

def add_task(conn, task):
   """
   Create a new task into the tasks table
   :param conn:
   :param task:
   :return: task id
   """
   sql = '''INSERT INTO tasks( project_id, name, description, status, start_date, end_date)
             VALUES(?,?,?,?,?,?)'''
   cur = conn.cursor()
   cur.execute(sql, task)
   conn.commit()
   return cur.lastrowid

def add_student(conn, student):
   """
   Create a new project into the students table
   :param conn:
   :param student:
   :return: id
   """
   sql = '''INSERT INTO students(first_name, last_name)
             VALUES(?,?)'''
   cur = conn.cursor()
   cur.execute(sql, student)
   conn.commit()
   return cur.lastrowid


#if __name__ == "__main__":
# """ Create Projects Table"""
create_projects_sql =  """ 
-- projects table
CREATE TABLE IF NOT EXISTS projects (
    id integer PRIMARY KEY,
    name text NOT NULL,
    start_date text,
    end_date text
);
"""
#""" Create Tasks Table """
create_tasks_sql =     """
-- zadanie table
CREATE TABLE IF NOT EXISTS tasks (
    id integer PRIMARY KEY,
    project_id integer NOT NULL,
    name VARCHAR(250) NOT NULL,
    description TEXT,
    status VARCHAR(15) NOT NULL,
    start_date text NOT NULL,
    end_date text NOT NULL,
    FOREIGN KEY (project_id) REFERENCES projects (id)
);
"""

#""" Create Studends Table """
create_students_sql =     """
-- zadanie table
CREATE TABLE IF NOT EXISTS students (
    id integer PRIMARY KEY,
    first_name VARCHAR(250) NOT NULL,
    last_name VARCHAR(250) NOT NULL
);
"""
#""" Insert into Tasks Table"""
insert_task_sql = """INSERT INTO tasks
(id, project_id, name, description, status, start_date, end_date)
VALUES (5,2,"fire members", "fire members of the project", "not started", "2024.01.10", "2024.01.14")
"""
db_file = "database.db"

conn = create_connection(db_file)
if conn is not None:
    #execute_sql(conn, create_projects_sql)
    #execute_sql(conn, create_tasks_sql)
    #execute_sql(conn, insert_project_sql)
    #execute_sql(conn, create_students_sql)
    #task = (2,"new begining", "cancel all the rent agreements for the project's activivies", "not started",  "2024.01.12", "2024.01.23") # Adding a task
    #tk_id = (add_task(conn, task));print(tk_id)
    #conn.close()
    #project = ("Polski", "2020-05-15 00:00:00", "2020-05-17 00:00:00") # Adding a project
    #pr_id = add_project(conn, project);print(f"pr_id = {pr_id}")
    #conn.close()
    #student = ("sarah","connor")
    #add_student(conn, student)
    #conn.close()






    """INSERT INTO projects
        (id, nazwa, start_date, end_date)
    VALUES (1,"Zr??b zadania", "2020-05-08 00:00:00","2020-05-10 00:00:00"
    );
    """

    
