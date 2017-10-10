# coding=utf-8
import pandas
import px_reader
import geopandas as gpd
import numpy as np
import matplotlib.pyplot as plt


# Read data
px_obj = px_reader.Px('A01S_HKI_Askan_rvuosi.px')
df = px_obj.pd_dataframe()
#df.to_csv('items.csv', encoding="utf-8")

# Read map data
# Use Geopandas to read the MapInfo files:
# a_hk_pie.DAT (The ASCII file that is the link between all other files and holds information about the type of data set file )
# a_hk_pie.ID  (Stores information linking graphic data to the database information. This contains a 4-byte integer index into the MAP file for each feature).
# a_hk_pie.MAP  (Stores the graphic and geographic information needed to display each vector feature on a map)
# a_hk_pie.tab (The ASCII file that is the link between all other files and holds information about the type of data set file )
kartta = gpd.read_file('./Seutukartta/SK-2016-avoin/a_hk_pie.tab')
#kartta.head()

kartta.plot()
plt.show()
#print('A_HK_per')
# Mikäli käytetään suoraan PcAxis –tiedostoa, aluenimi vaihdetaan aluekoodiksi 
# ”Muokkaa>Vaihda koodi/teksti” valikosta, jossa vaihdetaan Alue-muuttujan esitystavaksi koodi. 