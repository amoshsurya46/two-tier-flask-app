from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
import mysql.connector
import os
from datetime import datetime

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'dev-secret-key-change-in-production')

# Database configuration
DB_HOST = os.getenv('DB_HOST', 'mysql-db')
DB_USER = os.getenv('DB_USER', 'root')
DB_PASSWORD = os.getenv('DB_PASSWORD', 'password')
DB_NAME = os.getenv('DB_NAME', 'todoapp')

def get_db_connection():
    return mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME
    )

@app.route('/')
def index():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM todos ORDER BY created_at DESC")
        todos = cursor.fetchall()
        cursor.close()
        conn.close()
        return render_template('index.html', todos=todos)
    except Exception as e:
        return f"Database connection failed: {str(e)}"

@app.route('/add', methods=['POST'])
def add_todo():
    title = request.form['title']
    description = request.form.get('description', '')
    priority = request.form.get('priority', 'medium')
    
    if not title:
        flash('Title is required!', 'error')
        return redirect(url_for('index'))
    
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO todos (title, description, priority, status, created_at) VALUES (%s, %s, %s, %s, %s)",
        (title, description, priority, 'pending', datetime.now())
    )
    conn.commit()
    cursor.close()
    conn.close()
    
    flash('Todo added successfully!', 'success')
    return redirect(url_for('index'))

@app.route('/delete/<int:todo_id>')
def delete_todo(todo_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM todos WHERE id = %s", (todo_id,))
    conn.commit()
    cursor.close()
    conn.close()
    
    flash('Todo deleted successfully!', 'success')
    return redirect(url_for('index'))

@app.route('/toggle/<int:todo_id>')
def toggle_status(todo_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT status FROM todos WHERE id = %s", (todo_id,))
    current_status = cursor.fetchone()[0]
    
    new_status = 'completed' if current_status == 'pending' else 'pending'
    cursor.execute("UPDATE todos SET status = %s WHERE id = %s", (new_status, todo_id))
    conn.commit()
    cursor.close()
    conn.close()
    
    return redirect(url_for('index'))

@app.route('/edit/<int:todo_id>', methods=['GET', 'POST'])
def edit_todo(todo_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    if request.method == 'POST':
        title = request.form['title']
        description = request.form.get('description', '')
        priority = request.form.get('priority', 'medium')
        
        cursor.execute(
            "UPDATE todos SET title = %s, description = %s, priority = %s WHERE id = %s",
            (title, description, priority, todo_id)
        )
        conn.commit()
        cursor.close()
        conn.close()
        
        flash('Todo updated successfully!', 'success')
        return redirect(url_for('index'))
    
    cursor.execute("SELECT * FROM todos WHERE id = %s", (todo_id,))
    todo = cursor.fetchone()
    cursor.close()
    conn.close()
    
    return render_template('edit.html', todo=todo)

@app.route('/filter/<status>')
def filter_todos(status):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    if status == 'all':
        cursor.execute("SELECT * FROM todos ORDER BY created_at DESC")
    else:
        cursor.execute("SELECT * FROM todos WHERE status = %s ORDER BY created_at DESC", (status,))
    
    todos = cursor.fetchall()
    cursor.close()
    conn.close()
    
    return render_template('index.html', todos=todos, filter_status=status)

@app.route('/api/stats')
def get_stats():
    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Optimize with single query instead of multiple queries
    cursor.execute("""
        SELECT 
            COUNT(*) as total,
            SUM(CASE WHEN status = 'completed' THEN 1 ELSE 0 END) as completed,
            SUM(CASE WHEN status = 'pending' THEN 1 ELSE 0 END) as pending
        FROM todos
    """)
    result = cursor.fetchone()
    total, completed, pending = result
    
    cursor.close()
    conn.close()
    
    return jsonify({
        'total': total,
        'completed': completed,
        'pending': pending
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)