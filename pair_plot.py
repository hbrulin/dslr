import matplotlib.pyplot as plt
import sys
from analysis.describer import DataDescriber
from analysis.vis_utils import VUtils
from histogram import course_sub
from scatter_plot import courses_scatter

utils = VUtils

def pair_plot(data, courses):
    fig, axs = plt.subplots(13, 13, figsize=(12,7.5), tight_layout=True)
    for row_course, ax in zip(courses, axs):
        for col_course, ax_col in zip(courses, ax):
            if row_course == col_course:
                course_sub(ax_col, data, row_course)
            else:
                courses_scatter(data, [row_course, col_course], ax_col)
            ax_col.set_xticks([])
            ax_col.set_yticks([])
    plt.show()

def main():
    if (len(sys.argv) == 1) :
        print('\33[31m' +"Error: No input file." + '\33[0m')
        sys.exit()
    data = DataDescriber.get_data(sys.argv[1])
    courses = utils.get_courses(data)
    pair_plot(data, courses)

if __name__ == "__main__":
    main()