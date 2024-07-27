student_data = {}

num = 0
print('--'*16)
print('            WELCOME              ')
print('--'*16)
while True:
    #user input

    try:
        print(f'Student {num+1}')
        name = input('Enter name: ')
        age = int(input('Enter age: '))
        residence = input('Enter residence: ')
    except NameError:
        print('Please Enter Number')
    except ValueError:
        print('Please Enter Number')
    
    #Make key for student_data's dictionary and id for students
    id = 111+num
    key = 0+num
    num+=1

    students = {
        'id':id,
        'name':name,
        'age':age,
        'residence': residence
    }

    student_data.update({key:students})

    #Design
    for i in range(2):
        print('--'*16)
        if i<1:
            print('           DATABASE               ')

    #Get student's data and display 
    for i in student_data:
        key = i

        id = student_data[key]['id']
        name = student_data[key]['name']
        age = student_data[key]['age']
        residence = student_data[key]['residence']

        print(f' {id}   {name}    {age}   {residence}')
        print('--'*16)

    
    exit = input('Do you want to exit?(Y/N)\n')
    if exit == 'Y' or exit == 'y':
        
        print('=='*16+'\nThank you for using this system!\n'+'=='*16)
        break
    elif exit == 'N' or exit == 'n':
        pass
   

    
        

    
    
    
   

