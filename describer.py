import pandas as pd
import numpy as np
import sys

class DataDescriber(pd.DataFrame):
    def get_data(filename: str):
        try:
            data = pd.read_csv(filename)
        except :
            sys.exit("Error: File does not exist or has wrong format")
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

    #dropna removes missing value
    def count(self, feature: str):
        return len(self[feature].dropna())

    def mean(self, feature: str) -> float:
        return sum(self[feature].dropna()) / self.count(feature)
    
    #Tbdone
    def std(self, feature: str) -> float:
        return 0

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