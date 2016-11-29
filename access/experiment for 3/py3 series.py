import pandas as pd
import numpy as np
import matplotlib.pylab as plt
from matplotlib.pylab import rcParams
from pprint import pprint
rcParams['figure.figsize'] = 15, 6
dateparse = lambda dates: pd.datetime.strptime(dates, '%Y-%m')
data = pd.read_json('C:/Users/Grudger/Desktop/project_emas/data.json', parse_dates='time', index_col='time',date_parser=dateparse)
pprint(data)
