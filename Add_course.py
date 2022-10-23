import Course
import json
import File


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
        course_code=str(course_code)
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
        code=str(code)
        if code in Course.Course.available_course_codes:
            value=my_course.add_prerequisite(code)
            if value==1:
                print('No such course!')
                break
            if value==2:
                print('This course can not be added as prerequisite')
                continue
            elif value==3:
                print(f'Course with code: {code} added as prerequisite!')
                break
        else:
            now=input('There is no course with such id.Do you want to add this course?Press Y to add or any other to skip.')
            if now=='Y':
                course_title=take_course_title()
                credit=take_credit()
                new_course=Course.Course(code,course_title,credit)
                Course.Course.graph[code]=[my_course.course_code]
                Course.Course.in_degree[my_course.course_code]+=1
                Course.Course.available_course_codes[code]=1
                my_course.prerequisites.append(code)
                Courses=File.add_course_in_courses(new_course)
                File.save_courses(Courses)
                File.save_class_var()
                break
            else:
                break

def add_course(*args):
    if len(args)==1:
        course_code=args[0]
    else:
        course_code=take_course_code()
    course_title=take_course_title()
    credit=take_credit()
    my_course=Course.Course(course_code,course_title,credit)
    total=take_number_of_prerequisite()
    for i in range(total):
        take_prerequisite(my_course)
    else:
        print('Course has been added!')
    Courses=File.add_course_in_courses(my_course)
    File.save_courses(Courses)
    File.save_class_var()