import pandas as pd
import sys
from describer import DataDescriber
    
def print_table(data):
    rows = ["---", "Count", "Mean", "Std", "Min", "25%", "50%", "75%", "Max"]
    for row in rows:
        print(f'{row:>10}')
    for feature in data.columns:
        if data.is_numeric(feature) :
            print(f'{data.get_acronym(feature):>10}')
            print(f'{data.count(feature):>10}')
            print(f'{data.mean(feature):>10.6f}')

def main():
    if (len(sys.argv) == 1) :
        sys.exit("Error: No input dataset")
    data = DataDescriber.get_data(sys.argv[1])
    print_table(data)


if __name__ == "__main__":
    main()