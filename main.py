import pandas as pd
import numpy as np

from funcs.utils import read_yaml
from funcs.driver_functions import swebdriver

config = read_yaml()

zip = pd.read_csv("./data/uszips.csv")
zip = zip[zip['county_fips'].isin(config['fips'])]

driver = swebdriver(url = config['url'])

import pdb; pdb.set_trace()
