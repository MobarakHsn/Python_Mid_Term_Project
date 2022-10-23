import Course
import json

def write_in_json(file_name,obj):
    try:
        with open(file_name,'w') as file_object:
            json.dump(obj,file_object)
    except FileNotFoundError:
        print('Something went wrong!')

def read_from_json(file_name):
    try:
        with open(file_name) as file_object:
            x=json.load(file_object)
            return x
    except FileNotFoundError:
        print('Something went wrong!')

def save_class_var():
    x={
        "graph":Course.Course.graph,
        "in_degree":Course.Course.in_degree,
        "available_course_codes":Course.Course.available_course_codes
    }
    write_in_json("File1.json",x)

def save_courses(courses):
    write_in_json("File2.json",courses)

def add_course_in_courses(my_course):
    Courses=read_from_json('File2.json')
    Courses[my_course.course_code]={}
    Courses[my_course.course_code]['course_code']=my_course.course_code
    Courses[my_course.course_code]['course_title']=my_course.title
    Courses[my_course.course_code]['credit']=my_course.credit
    Courses[my_course.course_code]['prerequisites']=my_course.prerequisites
    return Courses