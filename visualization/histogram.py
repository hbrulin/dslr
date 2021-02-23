import matplotlib.pyplot as plt
import sys
from ../analysis/describer import DataDescriber

#Quel cours de Poudlard a une répartition des notes homogènes entre les quatres maisons ?
# en soi il est juste demandé de faire un plot par cours selon les maisons? Pas de comparaisons?
def histogram(data):
    #sort by house then use std on subset
    #le cours qui a le moins d'écart de variation std entre les houses

def set_plot(data):
    #legends etc...

def main():
    if (len(sys.argv) == 1) :
        print('\33[31m' +"Error: No input file." + '\33[0m')
        sys.exit()
    data = DataDescriber.get_data(sys.argv[1])
    set_plot(data)
    histogram(data)
    plt.show()


if __name__ == "__main__":
    main()