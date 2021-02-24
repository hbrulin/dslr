import matplotlib.pyplot as plt
import sys
import math
import numpy as np
from analysis.describer import DataDescriber
from utils.utils import Utils

#####Quel cours de Poudlard a une répartition des notes homogènes entre les quatres maisons ?####
def show_most_homogenous(data, course):
    for house, color in zip(data.houses, data.colors):
        grades = data[course][data['Hogwarts House'] == house].dropna()
        plt.hist(grades, color=color, alpha = 0.4)
    plt.title(f"Most homogeneous Hogwarts course:\n{course}")
    plt.ylabel("Number of students")
    plt.xlabel("Grades")
    plt.show()

"""
Algo: REVIEW!!!!!!!!!!!!!!!!
Calculate, for each house, the std variation of its grade for a given course.
Get the differences between each of these std variations with the total std variation for the course (all grades indifferent to houses), multiply by a 100 and ivide by std_course.
Add up those differences to get the combined difference of houses with regard to the std variation of the course.
Pick the smallest combined difference to get homogenous house.
"""
def get_house_diff(data, course, house):
    std_course = data.std(course)
    grades = data[course][data['Hogwarts House'] == house].dropna()
    mean = sum(grades) / len(grades)
    variance = sum((grades - mean)**2) / (len(grades) - 1)
    std_house = np.sqrt(variance)
    return std_course - std_house * 100 / std_course #ajout
        
def most_homogenous(data, courses):
    total_diff = []
    for i, course in enumerate(courses):
        house_diff = 0
        for house in data.houses:
                house_diff += get_house_diff(data, course, house)
        total_diff.append(house_diff)
    winner = total_diff.index(Utils.get_min(total_diff))
    print('\33[32m' + "%s is the most homogenous course!" %courses[winner] + '\33[0m')
    answer = input('\33[32m' + "Y to see its histogram : " + '\33[0m')
    if answer == "Y":
        show_most_homogenous(data, courses[winner])


####See all histograms####
def course_sub(ax, data, course):
    for house, color in zip(data.houses, data.colors):
        grades = data[course][data['Hogwarts House'] == house].dropna()
        ax.hist(grades, color=color, alpha = 0.4) #alpha for transparency


def courses_hist(data, courses):
    k = len(courses)
    nrows = math.ceil(k/3)
    ncols = 3
    fig = plt.figure(figsize=(12,7.5))
    plt.subplots_adjust(top=None, bottom=None, left=None, right=None, hspace=1.5, wspace=1)
    fig.suptitle('Courses house homogeneity')
    for i, course in enumerate(courses, start=1):
        ax = fig.add_subplot(nrows, ncols, i)
        ax.set(xlabel="Grades", ylabel="Students")
        ax.set_title(course)
        course_sub(ax, data, course)
    fig.legend(data.houses, loc="lower center",  borderaxespad=0.15)
    plt.show()


def main():
    if (len(sys.argv) == 1) :
        print('\33[31m' +"Error: No input file." + '\33[0m')
        sys.exit()
    data = DataDescriber.get_data(sys.argv[1])
    courses = Utils.get_courses(data)

    courses_hist(data, courses)
    plt.clf()
    most_homogenous(data, courses)

if __name__ == "__main__":
    main()