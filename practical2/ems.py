import Employee as em

employees = {}
command = 0
def display_menu():
    print('Select the program (1-5) to run: ')
    print('1. Search for an employee')
    print('2. Add new employee')
    print('3. Update employee details')
    print('4. Delete and employee')
    print('5. Quit the program')
    command = input('Enter your command (1-5) :')
    return int(command)

def display_employee(employee):
    print(employee)  #this statement will print the object because the Employee class has __str__

def search():
    id = input('Enter the employee id to search: ')
    if id in employees:
        #dictionary so employees[id] will give you the value which is the Employee object. Pass to display_empployee function, it will do the printing information
        display_employee(employees[id])
    else:
        print('id not found, try again!')


def add():
    id = input('Enter employee id: ')
    name = input('Enter employee name: ')
    title = input('Enter employee job title: ')
    department = input('Enter the department employee in: ')

    employee = em.Employee()
    employee.set_id(id)
    employee.set_name(name)
    employee.set_title(title)
    employee.set_department(department)
    employees[id] = employee  #add to the dictionary. key is id and value is the instance of Employee class

def update():
    id = input('Enter the employee id to change: ')
    if id in employees:
        name = input('What is the new name? (Leave empty to remain unchange): ')
        title = input('What is the new title? (Leave empty to remain unchange): ')
        department = input('What is the new department? (Leave empty to remain unchange): ')
        if len(name) > 0:
            employees[id].set_name(name)
        if len(title) > 0:
            employees[id].set_title(title)
        if len(department) > 0:
            employees[id].set_department(department)
        print(employees[id])
    else:
        print('id not found, try again!')


def delete():
    id = input('Enter the employee id to delete: ')
    if id in employees:
        employees.pop(id, None)
        # del employees[id]
        print('Employee', id, 'is deleted')
    else:
        print('id not found, try again!')

while True:
    val = display_menu()
    if val == 5:
        break
    elif val == 1:
        search()
    elif val == 2:
        add()
    elif val == 3:
        update()
    elif val == 4:
        delete()