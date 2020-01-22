import csv
import os

with open('people.csv', 'a', newline='') as file:
    writer = csv.writer(file, delimiter=',', quotechar='|',
                        quoting=csv.QUOTE_MINIMAL)

    # Check if the file already exists
    isFileEmpty = os.stat('people.csv').st_size == 0
    if isFileEmpty:
        # In case the file is empty, type in the title of each column
        writer.writerow(['First name', 'Last name', 'Salary'])

    while True:
        # Ask the user if they want to add more data
        print('Desea agregar un profesor a la nomina?')
        print('1. Si')
        print('2. No')
        answer = input()

        # Ask the employee's information
        if answer == '1':
            print('Nombre de el/la profesor(a):')
            firstname = input()

            print('Apellido(s) de el/la profesor(a):')
            lastname = input()

            print('Salario mensual:')
            salary = int(input())

            # Inser the data into the CSV file
            writer.writerow([firstname, lastname, salary])

        # Stop the program when the user is done adding data to the file
        elif answer == '2':
            print('Ok, bye!')
            break
        # Ask the user to pick one of the options by it's number
        else:
            print('Please try again and choose the number next to each option.')
