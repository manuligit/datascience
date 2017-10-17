#!/usr/bin/env python3
# coding=utf-8
import pandas as pd
import geopandas as gpd
import numpy as np
import matplotlib.pyplot as plt
import sys

# This project requires python3: 
if sys.version_info[0] < 3:
    raise Exception("Python 3 or a more recent version is required.")

# Read data
data = pd.read_csv('./kokotun.csv')

# Read map data
# Use Geopandas to read the MapInfo files:
# a_hk_pie.DAT (The ASCII file that is the link between all other files and holds information about the type of data set file )
# a_hk_pie.ID  (Stores information linking graphic data to the database information. This contains a 4-byte integer index into the MAP file for each feature).
# a_hk_pie.MAP  (Stores the graphic and geographic information needed to display each vector feature on a map)
# a_hk_pie.tab (The ASCII file that is the link between all other files and holds information about the type of data set file )
kartta = gpd.read_file('./Seutukartta/SK-2016-avoin/a_hk_pie.tab')
kartta.plot()
plt.show()