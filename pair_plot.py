import matplotlib.pyplot as plt
import sys
from analysis.describer import DataDescriber
from analysis.vis_utils import VUtils
from histogram import course_sub
from scatter_plot import courses_compare

utils = VUtils

def pair_plot(data, courses):
    fig, axs = plt.subplots(13, 13, figsize=(15,8), tight_layout=True)
    for row_course, ax in zip(courses, axs):
        for col_course, ax_col in zip(courses, ax):
            if row_course == col_course:
                course_sub(ax_col, data, row_course)
            else:
                courses_compare(data, [row_course, col_course], ax_col)
            ax_col.set_xticks([])
            ax_col.set_yticks([])
            if ax_col.is_last_row():
                ax_col.set_xlabel(data.get_acronym(col_course))
            if ax_col.is_first_col():
                label = data.get_acronym(row_course) if len(data.get_acronym(row_course)) < 6 else row_course[:6]
                ax_col.set_ylabel(label)
    plt.subplots_adjust(hspace=1, wspace=1)
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