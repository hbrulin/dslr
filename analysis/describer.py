import pandas as pd
import numpy as np
import sys

class DataDescriber(pd.DataFrame):

    houses = ['Gryffindor', 'Slytherin', 'Ravenclaw', 'Hufflepuff']
    colors = ['red', 'green', 'blue', 'yellow']

    ###general 

    def get_data(filename: str):
        try:
            data = pd.read_csv(filename)
        except :
            print('\33[31m' +"Error: File does not exist or has wrong format" + '\33[0m')
            sys.exit()
        return DataDescriber(data)

    def get_acronym(self, name: str):
        spl = name.split(" ")
        if (len(spl) <= 2):
            return name
        acronym = ""
        for word in spl :
            acronym += word[0].upper()
        return acronym

    def is_numeric(self, feature: str):
        return np.issubdtype(self[feature].dtype, np.number)

    
    ###description

    def count(self, feature: str):
        return len(self[feature].dropna()) #dropna removes missing value

    def mean(self, feature: str) -> float:
        return sum(self[feature].dropna()) / self.count(feature)
    
    """
    The standard deviation is a statistic that measures the dispersion of a dataset relative to its mean.
    The standard deviation is calculated as the square root of variance by determining each data point's deviation relative to the mean.
    If the data points are further from the mean, there is a higher deviation within the data set; thus, the more spread out the data, the higher the standard deviation.
    A volatile df has a high standard deviation, while the deviation of a homogenous df is usually rather low
    As a downside, the standard deviation calculates all uncertainty as risk/negative, even when deviation is caused by something good (ex: above-average returns).
    """
    def std(self, feature: str) -> float:
        variance = sum((self[feature].dropna() - self.mean(feature))**2) / (self.count(feature) - 1)
        return np.sqrt(variance)

    def min(self, feature: str) -> float:
        tmp = 0
        for nb in self[feature].dropna():
            if nb < tmp:
                tmp = nb
        return tmp

    def max(self, feature: str) -> float:
        tmp = 0
        for nb in self[feature].dropna():
            if nb > tmp:
                tmp = nb
        return tmp
    
    #quantile: x% of data is below the returned value
    def quantile(self, feature: str, percent: float) -> float:
        arr = sorted(self[feature].dropna())
        #calculate what rank is at percentile
        rank = (len(arr) - 1) * percent / 100

        #get floor : The floor of the scalar rank is the largest integer f, such that f <= x
        f = np.floor(rank)
        #get ceil : The ceil of the scalar x is the smallest integer i, such that i >= x.
        c = np.ceil(rank)
        #if same number, the rank corresponds to an existing value
        if f == c:
            return arr[int(rank)]
        d0 = arr[int(f)] * (c - rank)
        d1 = arr[int(c)] * (rank - f)
        return d0 + d1