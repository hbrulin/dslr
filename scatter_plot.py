import matplotlib.pyplot as plt
import sys
from analysis.describer import DataDescriber
from analysis.vis_utils import VUtils
import random

utils = VUtils

def courses_compare(data, courses, plot):
    for house, color in zip(data.houses, data.colors):
        x = data[courses[0]][data['Hogwarts House'] == house]
        y = data[courses[1]][data['Hogwarts House'] == house]
        plot.scatter(x, y, color=color, alpha=0.3)

def courses_scatter(data, courses, fig):
    for pos, course in enumerate(courses):
        for house, color in zip(data.houses, data.colors):
            grades = data[course][data['Hogwarts House'] == house].dropna()
            grades = (grades.astype(float) - data.min(course)) / (data.max(course) - data.min(course)) #scale between 0 and 1
            if len(grades) >= 50:
                grades = random.sample(list(grades), 50)
            X = [pos] * len(grades) #because x and y must be the same size for scatter
            plt.scatter(X, grades, color=color, alpha=0.3)
    plt.ylabel("Grades")
    plt.xticks(list(range(0, len(courses))), labels = courses)
    fig.autofmt_xdate() #so that xticks don't overlap
    plt.show()

def main():
    if (len(sys.argv) == 1) :
        print('\33[31m' +"Error: No input file." + '\33[0m')
        sys.exit()
    data = DataDescriber.get_data(sys.argv[1])
    
    courses = utils.get_courses(data)
    
    fig = plt.figure(figsize=(12,7.5))
    courses_scatter(data, courses, fig)
    plt.clf()
    
    #Ask compare two courses
    print('\33[32m' + "Scatter plot complete." + '\33[0m')
    answer = input('\33[32m' + "Y to compare two courses : " + '\33[0m')
    input_c = utils.get_input_courses(courses) if answer == "Y" else ""
    if input_c != "":
        courses_compare(data, input_c, plt)
        plt.xlabel(input_c[0])
        plt.ylabel(input_c[1])
        plt.show()
   
if __name__ == "__main__":
    main()