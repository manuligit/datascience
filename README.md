# Building / house types of Helsinki


### Data about buildings and house types

Helsinki city's statistical databases are open to everyone in [https://dev.hel.fi/apis/statistics/]().
There we found a further link to Helsinki's data series [http://www.aluesarjat.fi/](aluesarjat), where we chose
buildings database to examine.

The data was built from multiple files:

Tilastokanta > 

The data was in PC-Axis (.px) files, so we first had to convert them to .csv files with PC-AXis program.

...

Data can be connected to geo data by field 'kokotun', which is a
code for areas on Helsinki Seutukartta map.

### Geo data

We fetched Seutukartta 2016.zip from Helsinki Avoimet paikkatietoaineistot site 
(http://ptp.hel.fi/avoindata/), which serves geo data of Helsinki in MapInfo files.

For each part of map, the MapInfo files (.dat, .id, .map, .tab) were zipped and then converted to GeoJson files in
https://ogre.adc4gis.com/ (Source SRS: EPSG:3879, Target SRS: EPSG:4326).

We chose Helsingin peruspiirijako (A_HK_PER) as the map area division.

Folium (https://folium.readthedocs.io) is a library for python for drawing GeoJson on Maps. We added some color
according to the building type in the areas on the map.