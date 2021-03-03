import sys
import csv
from sklearn.metrics import accuracy_score
from analysis.describer import DataDescriber
from utils.utils import Utils, Action
from sorting_hat.multi_classifier import MultiClassifier
from histogram import get_houses_total_diff
from sorting_hat.predictor import Predictor

"""
#if issue with accuracy, don't use this because of arithmancy
def top_least_homogenous(data, courses):
     #answer = input('\33[32m' + "Y to train with non homogenous courses : " + '\33[0m')
    #if answer == "Y":
    #   courses = top_least_homogenous(data, courses) #not mandatory + if done i need to remove irrelevant y values : del data['Care of Magical Creatures']
    diff_arr = []
    for i, course in enumerate(courses):
        houses_diff = get_houses_total_diff(data, course)
        diff_arr.append([course, houses_diff])
    least_homo = sorted(diff_arr[:6]) #get last six elements
    #print(least_homo)
"""

def write_thetas(thetas):
    print('\33[32m' + "Calculated thetas are: " + '\33[0m')
    for theta in thetas:
        print(theta)
    with open("thetas.csv", 'w') as f:
        writer = csv.writer(f)
        for theta in thetas:
            writer.writerow(theta)


def main():
    ###deal with args
    if (len(sys.argv) == 1) :
        print('\33[31m' +"Error: No input file." + '\33[0m')
        sys.exit()
    show_plot = Utils.show_plot(sys.argv)
    
    ##get necessary data
    data = DataDescriber.get_data(sys.argv[1])
    courses = Utils.get_courses(data) #use least homogenous
    X, Y = Utils.normalize(data, courses, Action.TRAINING)
    m = len(X)

    ##train
    thetas = MultiClassifier.train(data, X, Y, m)
    write_thetas(thetas)

    #check accuracy by predicting dataset_train and comparing with existing
    predictions = Predictor.get_predictions(X, thetas)
    score = accuracy_score(Y, predictions) * 100
    print('\33[32m' + "Accuracy score is: %f %%" %score + '\33[0m')
    

   
if __name__ == "__main__":
    main()