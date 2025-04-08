from bottle import route, run, template, request
import sqlite3

conn = sqlite3.connect('payroll.db')
cursor = conn.cursor()

@route('/')
def index():
    return template('index')  # Assuming your index.tpl file is now named index.tpl

@route('/view_by_department')
def view_by_department():
    # Fetch departments from the database
    cursor.execute("SELECT DISTINCT department FROM employees")
    departments = [row[0] for row in cursor.fetchall()]
    return template('show_department', departments=departments)

@route('/view_by_department', method='POST')
def show_department():
    # Get the selected department from the form
    selected_department = request.forms.get('department')

    # Fetch employees from the selected department
    cursor.execute("SELECT * FROM employees WHERE department=?", (selected_department,))
    employees = cursor.fetchall()

    # Fetch departments from the database again
    cursor.execute("SELECT DISTINCT department FROM employees")
    departments = [row[0] for row in cursor.fetchall()]

    return template('show_department', departments=departments, selected_department=selected_department, employees=employees, dept=dept)

if __name__ == '__main__':
    run(host='localhost', port=8080, debug=True)
