import matplotlib.pyplot as plt
import sys
from analysis.describer import DataDescriber
from analysis.vis_utils import VUtils


#scatter matrix

def main():
    if (len(sys.argv) == 1) :
        print('\33[31m' +"Error: No input file." + '\33[0m')
        sys.exit()
    data = DataDescriber.get_data(sys.argv[1])
    courses = utils.get_courses(data)

    