import matplotlib.pyplot as plt
import sys
from analysis.describer import DataDescriber
from analysis.vis_utils import VUtils

utils = VUtils


def main():
    if (len(sys.argv) == 1) :
        print('\33[31m' +"Error: No input file." + '\33[0m')
        sys.exit()
    data = DataDescriber.get_data(sys.argv[1])
    
    courses = utils.get_courses(data)

    #courses_scatters(data, courses)
    #plt.clf()
    
    #later to compare two courses
    #input = utils.get_input_courses(courses)

if __name__ == "__main__":
    main()