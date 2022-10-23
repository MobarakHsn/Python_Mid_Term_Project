import Course
import Add_course as Add
import File

courses={}

def load_data_from_file():
    x=File.read_from_json('File1.json')
    Course.Course.graph=x['graph']
    Course.Course.in_degree=x['in_degree']
    Course.Course.available_course_codes=x['available_course_codes']

def take_option():
    while True:
        option=input('Please, choose an options: ');
        try:
            option=int(option)
        except ValueError:
            print('Please enter only integers')
            continue
        if  option>=0 and option<=5:
            break;
        else:
            print('Options range available from 0 to 5 only')
    return option

def display_all():
    cnt=0
    for i in courses:
        cnt+=1
        print(f"({cnt})")
        print(f"Course code: {courses[i]['course_code']}")
        print(f"Course title: {courses[i]['course_title']}")
        print(f"Course credit: {courses[i]['credit']}")
        print(f"Prerequisite course codes: {courses[i]['prerequisites']}")

def delete_course(course_code):
    if course_code not in Course.Course.available_course_codes:
        print('No matched course found!')
    else:
        for i in Course.Course.graph:
            try:
                Course.Course.graph[i].remove(course_code)
            except ValueError:
                continue
        del Course.Course.graph[course_code]
        del Course.Course.in_degree[course_code]
        del Course.Course.available_course_codes[course_code]

        for i in courses:
            try:
                courses[i]['prerequisites'].remove(course_code)
            except ValueError:
                continue
        del courses[course_code]
        File.save_class_var()
        File.save_courses(courses)

def search_course():
    while True:
        code=input('Enter the code of the course you are searching for: ')
        try:
            code=int(code)
        except ValueError:
            print('Please enter only integers')
            continue
        break
    course_code=str(code)
    if course_code in Course.Course.available_course_codes:
        print(f"Course code: {courses[course_code]['course_code']}")
        print(f"Course title: {courses[course_code]['course_title']}")
        print(f"Course credit: {courses[course_code]['credit']}")
        print(f"Prerequisite course codes: {courses[course_code]['prerequisites']}")
    else:
        now=input('This course is not available do you want to add this course?Press Y to add and any other to skip:')
        if now=='Y':
            Add.add_course(course_code)

def update_existing_course():
    course_code=input('Enter course code of the course you want to update: ')
    if course_code not in Course.Course.available_course_codes:
        print('No matched course found!')
    else:
        my_course=Course.Course(0,'x',0)
        my_course.course_code=course_code
        my_course.title=courses[course_code]['course_title']
        my_course.credit=courses[course_code]['credit']
        my_course.prerequisites=courses[course_code]['prerequisites']
        print(f"Old course title: {courses[course_code]['course_title']}")
        x=input('Do you want to change it?Press Y to change and any other to skip.')
        if x=='Y':
            title=input('New course title: ')
            courses[course_code]['course_title']=title
        print(f"Old course credit: {courses[course_code]['credit']}")
        x=input('Do you want to change it?Press Y to change and any other to skip.')
        if x=='Y':
            credit=input('New course credit: ')
            courses[course_code]['credit']=credit
        x=input('Do you add some prerequisite course?Press Y to add and any other to skip.')
        if x=='Y':
            total=Add.take_number_of_prerequisite()
            for i in range(total):
                Add.take_prerequisite(my_course)
            courses[course_code]['prerequisites']=my_course.prerequisites
        File.save_courses(courses)
        File.save_class_var()

while True:
    courses=File.read_from_json('File2.json')
    load_data_from_file()
    print('***********************************************')
    print('*** Enter 1 for adding a new course         ***')
    print('*** Enter 2 for updating an existing course ***')
    print('*** Enter 3 for deleting an existing course ***')
    print('*** Enter 4 for displaying all the course   ***')
    print('*** Enter 5 for searching a course          ***')
    print('*** Enter 0 for exit                        ***')
    print('***********************************************')
    option=take_option()
    if option==0:
        break
    elif option==1:
        Add.add_course()
    elif option==2:
        update_existing_course()
    elif option==3:
        x=input('Enter the course code you want to remove: ')
        delete_course(x)
    elif option==4:
        display_all()
    elif option==5:
        search_course()