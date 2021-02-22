import pandas as pd
import sys
from describer import DataDescriber
    
def print_table(data):
    print("")
    print(f'{"":15} {"Count":>12} {"Mean":>12} {"Std":>12} {"Min":>13}'
          f'{"Max":>12} {"25%":>12} {"50%":>12} {"75%":>12}')
    print("")
    for feature in data.columns:
        if data.is_numeric(feature) :
            print(f'{data.get_acronym(feature):>15} {data.count(feature):>11} {data.mean(feature):>15.4f} {data.std(feature):>11.4f} {data.min(feature):>13.4f} {data.max(feature):>12.4f}')

def main():
    if (len(sys.argv) == 1) :
        sys.exit("Error: No input dataset")
    data = DataDescriber.get_data(sys.argv[1])
    print_table(data)


if __name__ == "__main__":
    main()