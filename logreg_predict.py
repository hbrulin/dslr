import numpy as np
import sys
import csv
from analysis.describer import DataDescriber
from utils.utils import Utils, Action
from sorting_hat.predictor import Predictor

def get_thetas():
    with open("thetas.csv") as f:
        dt = csv.reader(f)
        thetas = []
        for _ in range(4):
            theta = np.array(next(dt)).astype(float)
            thetas.append(theta)
    return thetas

def write_predictions(data, predictions):
    with open("houses.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerow(["Index", "Hogwarts House"])
        for i, house_nb in enumerate(predictions):
            writer.writerow([i, data.houses[house_nb]])

def main():
    ###deal with arguments
    if (len(sys.argv) == 1) :
        print('\33[31m' +"Error: No input file." + '\33[0m')
        sys.exit()
    show_plot = Utils.show_plot(sys.argv)

    ###get necessary data
    data = DataDescriber.get_data(sys.argv[1])
    courses = Utils.get_courses(data)
    X, Y = Utils.normalize(data, courses, Action.PREDICTION)
    thetas = get_thetas()

    ###predict
    predictions = Predictor.get_predictions(X, thetas)
    write_predictions(data, predictions)
    

if __name__ == "__main__":
    main()