import Course
obj=Course.Course(1,'Python',2)

def take_number_of_prerequisite():
    while True:
        number=input('Enter number of prerequisites: ')
        try:
            number=int(number)
        except ValueError:
            print('Please enter only integers')
            continue
        break
    return number

def take_course_code():
    while True:
        course_code=input('Enter an integer course code: ')
        try:
            course_code=int(course_code)
        except ValueError:
            print('Please enter only integers')
            continue
        if course_code in Course.Course.available_course_codes:
            print('Course code already in use enter a new one')
            continue
        else:
            break
    return course_code
def take_course_title():
    course_title=input('Enter course title: ')
    return course_title

def take_credit():
    while True:
        credit=input('Enter course credit between 1 to 3: ')
        try:
            credit=int(credit)
        except ValueError:
            print('Please enter only integers')
            continue
        if credit>=1 and credit<=3:
            break;
        else:
            print('Credit must be in range 1 to 3')
    return credit

def take_prerequisite(my_course):
    while True:
        code=input('Enter an integer course code: ')
        try:
            code=int(code)
        except ValueError:
            print('Please enter only integers')
            continue
        if code in Course.Course.available_course_codes:
            value=my_course.add_prerequisite(code)
            if value==2:
                print('This course can not be added as prerequisite')
                continue
            break
        else:
            now=input('There is no course with such id.Do you want to add this course?Press Y to add or any other to skip.')
            if now=='Y':
                course_title=take_course_title()
                credit=take_credit()
                new_course=Course.Course(code,course_title,credit)
                my_course.prerequisites.append(code)
                break
            else:
                break

def add_course():
    course_code=take_course_code()
    course_title=take_course_title()
    credit=take_credit()
    my_course=Course.Course(course_code,course_title,credit)
    total=take_number_of_prerequisite()
    for i in range(total):
        take_prerequisite(my_course)
    
def take_option():
    while True:
        option=input('Please, choose an options: ');
        try:
            option=int(option)
        except ValueError:
            print('Please enter only integers')
            continue
        if  option>=0 and option<=4:
            break;
        else:
            print('Options range available from 0 to 4 only')
    return option

while True:
    print('Enter 1 for adding a new course')
    print('Enter 2 for updating an existing course')
    print('Enter 3 for deleting an existing course')
    print('Enter 4 for displaying all the course')
    print('Enter 0 for exit')
    option=take_option()
    if option==0:
        break
    elif option==1:
        add_course()