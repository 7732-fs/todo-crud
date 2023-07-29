import sqlite3
from classes.classes import Task

def get_tasks():
    tasks=[]
    tasks_from_db=read()
    for task_tuple in tasks_from_db:
        tid=task_tuple[0]
        name=task_tuple[1]
        description=task_tuple[2]
        task=Task(tid, name, description)
        tasks.append(task)
    return tasks

def query_db(sql_query):
    with sqlite3.connect("todo.db") as conn:
        cur=conn.cursor()
        cur.execute("CREATE TABLE IF NOT EXISTS todo (id INTEGER PRIMARY KEY, category TEXT, description TEXT, date TEXT)")
        cur.execute(sql_query)
        return cur.fetchall()

def add(task:Task, table='todo'):
    query_db(f"INSERT INTO {table} (category, description, date) VALUES ('{task.category}', '{task.description}', '{task.date}')")

def update(table, column, value, id):
    query_db(f"UPDATE {table} SET {column}='{value}' WHERE id={int(id)}")

def read(table="todo"):
    return query_db(f"SELECT * FROM {table}")

def delete(id, table="todo"):
    return query_db(f"DELETE FROM {table} WHERE id={int(id)}")

def update(task:Task):
    query_db(f"UPDATE todo SET description='{task.description}', category='{task.category}' WHERE id={task.tid}")

def get_task(tid):
    return query_db(f"SELECT * FROM todo WHERE id={tid}")
