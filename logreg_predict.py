import matplotlib.pyplot as plt
import numpy as np
import sys
import csv
from analysis.describer import DataDescriber
from utils.utils import Utils
from sorting_hat.predictor import Predictor


def main():
    if (len(sys.argv) == 1) :
        print('\33[31m' +"Error: No input file." + '\33[0m')
        sys.exit()
    show_plot = Utils.show_plot(sys.argv)
    
    #get grades
    data = DataDescriber.get_data(sys.argv[1])
    courses = Utils.get_courses(data)
    X = np.array(data[courses])
    X = np.nan_to_num(X, nan=1)
    X = (X - X.min()) / (X.max() - X.min())

    #get thetas
    with open("thetas.csv") as f:
        dt = csv.reader(f)
        thetas = []
        for _ in range(4):
            theta = np.array(next(dt)).astype(float)
            thetas.append(theta)

    print(thetas)
    predictions = Predictor.get_predictions(X, thetas)

    with open("houses.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerow(["Index", "Hogwarts House"])
        for i, house_nb in enumerate(predictions):
            write.writerow([i, data['Hogwarts House'][house_nb]])

if __name__ == "__main__":
    main()