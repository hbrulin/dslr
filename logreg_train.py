import matplotlib.pyplot as plt
import sys
from analysis.describer import DataDescriber
from utils.utils import Utils
from sorting_hat.multi_classifier import MultiClassifier
from histogram import get_houses_total_diff

def top_least_homogenous(data, courses):
    diff_arr = []
    for i, course in enumerate(courses):
        houses_diff = get_houses_total_diff(data, course)
        diff_arr.append([course, houses_diff])
    least_homo = sorted(diff_arr[:6]) #get last six elements
    #print(least_homo)
    #if issue with accuracy, don't use this because of arithmancy

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
    opti = Utils.opto(sys.argv)
    
    data = DataDescriber.get_data(sys.argv[1])
    courses = Utils.get_courses(data)
    if opti == True:
        courses = top_least_homogenous(data, courses) #not mandatory

    #init_train(data, courses)
    #train()

    
   
if __name__ == "__main__":
    main()