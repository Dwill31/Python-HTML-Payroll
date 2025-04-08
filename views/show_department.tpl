<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>View Employees by Department</title>
</head>
<body>
    <h2>Get Payroll by Department</h2>
    <form action="/view_by_department" method="POST">
        <label for="department">Select Department:</label>
        <select name="department" id="department">
            {% for dept in departments %}
                <option value="{{ dept }}" {% if selected_department == dept %} selected {% endif %}>{{ dept }}</option>
            {% endfor %}
        </select>
        <button type="submit">Submit</button>
    </form>

    {% if employees %}
        <h2>Employees in Department: {{ selected_department }}</h2>
        <ul>
            {% for employee in employees %}
                <li>{{ employee.name }} - {{ employee.hours_worked }}</li>
            {% endfor %}
        </ul>
    {% endif %}
</body>
</html>
