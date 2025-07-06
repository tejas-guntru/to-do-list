from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime, date

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # Required for flash messages

tasks = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add', methods=['GET', 'POST'])
def add_task():
    if request.method == 'POST':
        task = request.form.get('task', '').strip()
        deadline_str = request.form.get('deadline', '').strip()
        
        if not task:
            flash('Task description cannot be empty!', 'error')
            return redirect(url_for('add_task'))
        
        try:
            deadline = datetime.strptime(deadline_str, '%Y-%m-%d').date() if deadline_str else None
        except ValueError:
            flash('Invalid date format. Please use YYYY-MM-DD.', 'error')
            return redirect(url_for('add_task'))
        
        task_data = {
            'task': task,
            'added': date.today(),
            'deadline': deadline
        }
        
        tasks.append(task_data)
        flash('Task added successfully!', 'success')
        return redirect(url_for('view_tasks'))
    
    return render_template('add_task.html')

@app.route('/view')
def view_tasks():
    today = date.today()
    for task in tasks:
        if task['deadline']:
            task['status'] = 'Overdue' if task['deadline'] < today else 'Pending'
        else:
            task['status'] = 'No deadline'
    
    return render_template('view_tasks.html', 
                         tasks=tasks,
                         datetime=datetime,  # Make datetime available in template
                         now=date.today())  # Current date for comparison

@app.route('/delete/<int:task_id>')
def delete_task(task_id):
    if 0 <= task_id < len(tasks):
        removed_task = tasks.pop(task_id)
        flash(f"Task '{removed_task['task']}' removed!", 'success')
    else:
        flash('Invalid task ID!', 'error')
    return redirect(url_for('view_tasks'))

if __name__ == '__main__':
    app.run(debug=True)