import matplotlib.pyplot as plt
#Quelles sont les deux features qui sont semblables ?





def main():
    if (len(sys.argv) == 1) :
        print('\33[31m' +"Error: No input file." + '\33[0m')
        sys.exit()
    data = DataDescriber.get_data(sys.argv[1])

if __name__ == "__main__":
    main()