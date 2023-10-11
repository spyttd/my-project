from flask import Flask, render_template

app = Flask(__name__)

# Load employee data from CSV
def load_employees_from_csv():
    try:
        with open('employees.csv', 'r') as file:
            reader = csv.reader(file)
            global employees
            employees = list(reader)
    except FileNotFoundError:
        employees = []

# Save employee data to CSV
def save_employees_to_csv():
    with open('employees.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(employees)

# Define routes and views
@app.route('/')
def index():
    # Load employees and pass them to the template
    load_employees_from_csv()
    return render_template('index.html', employees=employees)

@app.route('/add_employee')
def add_employee():
    # Render the add employee form
    return render_template('add_employee.html')

@app.route('/edit_employee')
def edit_employee():
    # Render the edit employee form
    return render_template('edit_employee.html')

@app.route('/mark_attendance')
def mark_attendance():
    # Render the mark attendance form
    return render_template('mark_attendance.html')

@app.route('/view_salary')
def view_salary():
    # Render the view salary form
    return render_template('view_salary.html')

if __name__ == '__main__':
    app.run(debug=True)
