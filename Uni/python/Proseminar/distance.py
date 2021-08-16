import math

class DistanceModel:

    def __init__(self, attributes):
        self.attributes = attributes
    
    def get_distance(self, d1, d2):
        sum = 0
        for a in self.attributes:
            sum += math.pow(d1[a]-d2[a], 2)
        return math.sqrt(sum)