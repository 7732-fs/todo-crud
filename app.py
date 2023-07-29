from flask import Flask, render_template, request, redirect, url_for, flash, get_flashed_messages
import db.crud as crud
from classes.classes import Task
import db

app = Flask(__name__)

@app.route('/list')
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method=='GET':
        tasks=[]
        tasks_from_db=crud.read()
        for task_tuple in tasks_from_db:
            tid=task_tuple[0]
            category=task_tuple[1]
            description=task_tuple[2]
            date=task_tuple[3]
            task=Task(tid, category, description, date)
            tasks.append(task)
        return render_template("index.html", tasks=tasks)

@app.route('/update', methods=['GET', 'POST'])
def update():
    tasks=[]
    if request.method=='GET':
        tasks_from_db=crud.read()
        for task_tuple in tasks_from_db:
            tid=task_tuple[0]
            name=task_tuple[1]
            description=task_tuple[2]
            date=task_tuple[3]
            task=Task(tid, name, description, date)
            tasks.append(task)
        return render_template("update.html", tasks=tasks, categories=Task.categories)
    else:
        tid=request.form["id"]
        category=request.form["category"]
        description=request.form["description"]
        task=Task(tid=tid, description=description, category=category)
        crud.update(task)
        return redirect(url_for('home'))

@app.route('/update/task/<tid>', methods=['GET', 'POST'])
def update_task(tid):
    if request.method=='POST':
        crud.update(Task(tid=tid, category=request.form["category"], description=request.form["description"], date=request.form["date"]))
        return redirect(url_for('home'))
    else:
        task=Task(*crud.get_task(tid)[0])
        return render_template("task.html", task=task)

@app.route('/add', methods=['POST', 'GET'])
def add():
    if request.method=='POST':
        task=Task(description=request.form["description"], category=request.form["category"], date=request.form["date"])
        task.add()
        return redirect(url_for('home'))
    return render_template('add.html', categories=Task.categories)

@app.route('/delete', methods=['GET', 'POST'])
def method_name():
    if request.method=='POST':
        crud.delete(request.form["id"])
        return redirect(url_for('home'))
    else:
        return render_template("delete.html")


@app.before_request
def authorize():
    if "add" in request.path:
        return 
