# The usage of buildings in Helsinki


### Building data

...

about data

...

Data can be connected to geo data by field 'kokotun', which is a
code for certain areas on map.

### Geo data

Fetched Seutukartta 2016.zip from Helsinki Avoimet paikkatietoaineistot site 
(http://ptp.hel.fi/avoindata/), which serves geo data of Helsinki in MapInfo files.

For each part of map, the MapInfo files (.dat, .id, .map, .tab) were zipped and then converted to GeoJson files in
https://ogre.adc4gis.com/ (Source SRS: EPSG:3879, Target SRS: EPSG:4326).

Map parts for Helsinki are:
- Helsingin pienaluejako A_HK_PIE
- Helsingin osa-aluejako A_HK_OSA
- Helsingin peruspiirijako A_HK_PER
- Helsingin suurpiirijako A_HK_SUU

Folium (https://folium.readthedocs.io) is a library for python for drawing GeoJson to Maps.