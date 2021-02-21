import pandas as pd
import sys

def get_data(filename) :
    df = pd.read_csv(filename)
    try:
        df = pd.read_csv(filename)
    except :
        sys.exit("Error: File does not exist or has wrong format")

    ari = df.iloc[0:len(df),6]
    astr = df.iloc[0:len(df),7]
    herb = df.iloc[0:len(df),8]
    dada = df.iloc[0:len(df),9]
    div = df.iloc[0:len(df),10]
    mug = df.iloc[0:len(df),11]
    runes = df.iloc[0:len(df),12]
    hist = df.iloc[0:len(df),13]
    trans = df.iloc[0:len(df),14]
    pot = df.iloc[0:len(df),15]
    comc = df.iloc[0:len(df),16]
    charms = df.iloc[0:len(df),17]
    fly = df.iloc[0:len(df),18]
    print(fly)
    
    
    #m = len(ari)
    

def main():
    if (len(sys.argv) == 1) :
        sys.exit("Error: No input dataset")
    get_data(sys.argv[1])


if __name__ == "__main__":
    main()