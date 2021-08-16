from outlier import OutlierModel
from distance import DistanceModel
from data import DataModel
import math

data_model = DataModel('daily_hunting_season_environmental_conditions.csv')
data = data_model.get_data()
attributes = ['temp_max', 'temp_min', 'temp_mean', 'water_level']
distance_model = DistanceModel(attributes)
d = math.sqrt(sum(math.pow(data_model.get_average(a), 2) for a in attributes))/4.5

outlier_model = OutlierModel(25, d, distance_model, data)

for object in data:
    if(outlier_model.is_outlier(object)):
        print(object)