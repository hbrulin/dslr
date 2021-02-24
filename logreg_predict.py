import matplotlib.pyplot as plt
import sys
from analysis.describer import DataDescriber
from utils.utils import Utils
from sorting_hat.predictor import Predictor


def main():
    if (len(sys.argv) == 1) :
        print('\33[31m' +"Error: No input file." + '\33[0m')
        sys.exit()
    show_plot = Utils.show_plot(sys.argv)
    
    data = DataDescriber.get_data(sys.argv[1])

    #get student data
    #get thetas
    predictions = Predictor.get_predictions(stud_data, thetas)

    with open("houses.csv", "w") as f:
        writer = csv.writer(f)
        writer.writerow(["Index", "Hogwarts House"])
        for i, house_nb in enumerate(predictions)
            write.writerow([i, data['Hogwarts House'][house_nb]])

if __name__ == "__main__":
    main()