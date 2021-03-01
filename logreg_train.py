import matplotlib.pyplot as plt
import numpy as np
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

def main():
    if (len(sys.argv) == 1) :
        print('\33[31m' +"Error: No input file." + '\33[0m')
        sys.exit()
    show_plot = Utils.show_plot(sys.argv)
    
    data = DataDescriber.get_data(sys.argv[1])
    courses = Utils.get_courses(data)

    #answer = input('\33[32m' + "Y to train with non homogenous courses : " + '\33[0m')
    #if answer == "Y":
    #   courses = top_least_homogenous(data, courses) #not mandatory + if done i need to remove irrelevant y values : del data['Care of Magical Creatures']

    X = np.array(data[courses])
    X = np.nan_to_num(X, nan=1)
    Y = np.array(data["Hogwarts House"])
    m = len(X)
    thetas = MultiClassifier.train(data, X, Y, m)
    for theta in thetas:
        print(theta)

    
   
if __name__ == "__main__":
    main()