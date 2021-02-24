import matplotlib.pyplot as plt
import sys
from analysis.describer import DataDescriber
from utils.utils import Utils
from sorting_hat.multi_classifier import MultiClassifier
from histogram import get_houses_total_diff

def top_least_homogenous(data, courses):
    #smallest_diff = ["", 0.0]
    for i, course in enumerate(courses):
        houses_diff = get_houses_total_diff(data, course)
        print("%s: %f" %(course, houses_diff))
        """
        if i == 0:
            smallest_diff = [course, houses_diff]
        elif smallest_diff[1] > houses_diff:
            smallest_diff = [course, houses_diff]
        """
    ###change for biggest and set min heterogeneity

"""

def init_train(data, relevant_courses):

    #get data
     #select non homogenous courses?
    x = data[courses]
    y = 
    m = 

    #normalize data

    #launch model computations
    model = MultiClassifier()
"""

def main():
    if (len(sys.argv) == 1) :
        print('\33[31m' +"Error: No input file." + '\33[0m')
        sys.exit()
    show_plot = Utils.show_plot(sys.argv)
    
    data = DataDescriber.get_data(sys.argv[1])
    courses = Utils.get_courses(data)
    courses = top_least_homogenous(data, courses) #not mandatory

    #init_train(data, courses)
    #train()

    
   
if __name__ == "__main__":
    main()