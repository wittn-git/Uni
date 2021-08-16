import pandas as pd
import numpy as np

class DataModel:

    def __init__(self, filename):
        self.data = pd.read_csv(filename)
    
    def get_data(self):
        return self.data

    def get_attr_list(self, attr):
        print((d[attr] for d in self.data.loc))
        return 0

    def get_average(self, attr):
        attrs = self.get_attr_list(attr)
        print(attrs)
        return np.mean(attrs)
    
    def get_min(self, attr):
        attrs = self.get_attr_list(attr)
        return np.min(attrs)

    def get_max(self, attr):
        attrs = self.get_attr_list(attr)
        return np.max(attrs)