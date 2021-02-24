import matplotlib.pyplot as plt
import sys
from analysis.describer import DataDescriber
from utils.utils import Utils
from sorting_hat.multi_classifier import MultiClassifier



def init_train(data):

    #get data
    courses = utils.get_courses(data) #select non homogenous courses?
    x = data[courses]
    y = 
    m = 

    #normalize data

    #launch model computations
    model = MultiClassifier()


def main():
    if (len(sys.argv) == 1) :
        print('\33[31m' +"Error: No input file." + '\33[0m')
        sys.exit()
    show_plot = Utils.show_plot(sys.argv)
    
    data = DataDescriber.get_data(sys.argv[1])

    init_train(data)
    #train()

    
   
if __name__ == "__main__":
    main()