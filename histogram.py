import matplotlib.pyplot as plt
import sys
from analysis.describer import DataDescriber

#Quel cours de Poudlard a une répartition des notes homogènes entre les quatres maisons ?

def course_sub(ax, data, course):
    ax.set_title(course)
    for house, color in zip(data.houses, data.colors):
        grades = data[course][data['Hogwarts House'] == house].dropna()
        ax.hist(grades, color=color)


def courses_hist(data, courses):
    fig, axs = plt.subplots(len(courses))
    fig.suptitle('Courses subplots')
    #The enumerate() function assigns an index to each item in an iterable object that can be used to reference the item later.
    for i, course in enumerate(courses):
        course_sub(axs[i], data, course)
    plt.show()


def main():
    if (len(sys.argv) == 1) :
        print('\33[31m' +"Error: No input file." + '\33[0m')
        sys.exit()
    data = DataDescriber.get_data(sys.argv[1])
    courses = []
    for feature in data.columns:
        if data.is_numeric(feature) and feature != "Index":
            courses.append(feature)

    #faire un histogramme par cours selon les maisons
    courses_hist(data, courses)

    #calculer variation selon les maisons pour chaque cours et display cette variation sur un histogramme qui représente chaque cours




if __name__ == "__main__":
    main()