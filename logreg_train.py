import sys
import csv
from sklearn.metrics import accuracy_score
from analysis.describer import DataDescriber
from utils.utils import Utils, Action
from sorting_hat.multi_classifier import MultiClassifier
from histogram import get_houses_total_diff
from sorting_hat.predictor import Predictor

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

    ##get necessary data
    data = DataDescriber.get_data(sys.argv[1])
    courses = data.get_courses()
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