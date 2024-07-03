from flask import Flask, render_template, request, redirect, url_for
from todo_list import ToDoList

app = Flask(__name__)
to_do_list = ToDoList()

@app.route('/')
def index():
    tasks = to_do_list.view_tasks()
    return render_template('index.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add():
    description = request.form['description']
    to_do_list.add_task(description)
    return redirect(url_for('index'))

@app.route('/complete/<int:task_id>')
def complete(task_id):
    to_do_list.complete_task(task_id)
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>')
def delete(task_id):
    to_do_list.delete_task(task_id)
    return redirect(url_for('index'))

@app.route('/update/<int:task_id>', methods=['POST'])
def update(task_id):
    new_description = request.form['description']
    to_do_list.update_task(task_id, new_description)
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
