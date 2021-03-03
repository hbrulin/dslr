import pandas as pd
import sys
import numpy as np
from enum import Enum, auto

class Action(Enum):
    TRAINING = auto()
    PREDICTION = auto()

class Utils:
    ###general
    def get_courses(data):
        courses = []
        for feature in data.columns:
            if data.is_numeric(feature) and feature != "Index" and feature != "Hogwarts House":
                courses.append(feature)
        return courses

    ###sorting hat
    def normalize(data, courses, action):
        X = []
        Y = []
        for i, row in data.iterrows():
            normalized = []
            #print(row[courses].values)
            for course in courses:
                #print(row[course])
                try:
                    normalized.append(
                        (row[course] - data.mean(course)) / data.std(course) #this way to normalize gets higher accuracy than min-max
                    )
                except:
                    normalized.append(0) #pourquoi ça ça ne vire pas les nan?
            X.append(normalized)
            if action == Action.TRAINING:
                Y.append(data.houses.index(row[1])) #index nb of house
        X = np.nan_to_num(X, nan=1)
        return [X, Y]

    ###Visualisation
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