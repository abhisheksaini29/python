# Given a dictionary employee_details where the keys are employee IDs and values are dictionaries with name, department, and salary, filter and 
# create a list of names of employees who have a salary greater than 50,000.

employee_details = {
        1: {'name': 'Alice', 'department': 'HR', 'salary': 60000},
        2: {'name': 'Bob', 'department': 'Engineering', 'salary': 45000},
        3: {'name': 'Charlie', 'department': 'Marketing', 'salary': 70000},
        4: {'name': 'David', 'department': 'Sales', 'salary': 55000},
        5: {'name': 'Eve', 'department': 'Engineering', 'salary': 48000}
}
high_salary_employees = [details['name'] for details in employee_details.values() if details['salary'] > 50000]
print("Employees with a salary greater than 50,000:")
print(high_salary_employees)