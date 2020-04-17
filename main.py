import pandas as pd
import numpy as np
import yaml

from selenium import webdriver 
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException

def read_yaml(fl = "config.yaml"):
    with open(fl, 'r') as stream:
        try:
            return yaml.safe_load(stream)
        except yaml.YAMLError as exc:
            return exc

config = read_yaml()

zip = pd.read_csv("./data/uszips.csv")
zip = zip[zip['county_fips'].isin(config['fips'])]

import pdb; pdb.set_trace()
