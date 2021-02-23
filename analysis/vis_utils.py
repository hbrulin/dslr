import pandas as pd
import sys

class VUtils:

    def get_courses(data):
        courses = []
        for feature in data.columns:
            if data.is_numeric(feature) and feature != "Index":
                courses.append(feature)
        return courses

    def ask_for_course(courses, nb):
        check_course = False
        while check_course == False :
            course = input('\33[33m' + "Enter %s Course: " %nb + '\33[0m')
            if course in courses:
                check_course = True
            else:
                print('\33[31m' +"Error: Course does not exist" + '\33[0m')
        return course

    def get_input_courses(courses):
        print('\33[33m' + "Pick the two courses you want to compare among the following:" + '\033[0m')
        for i, course in enumerate(courses):
            if i == len(courses) - 1:
                print('\33[94m' + course + '\33[0m')
            else:
                print('\33[94m' + course, " | " + '\33[0m', end='')

        courseA = VUtils.ask_for_course(courses, "First")
        courseB = VUtils.ask_for_course(courses, "Second")

        return [courseA, courseB]