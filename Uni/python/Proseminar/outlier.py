class OutlierModel:

    def __init__(self, p, d, distance_model, data):
        self.p = p
        self.d = d
        self.distance_model = distance_model
        self.data = data
    
    def is_outlier(self, object):
        count = 0
        for k in self.data:
            if self.distance_model.get_distance(object, k) > self.d:
                count += 1
        if 100/len(self.data)*count > self.p: return True
        return False