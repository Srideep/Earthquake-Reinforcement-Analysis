import pandas as pd
import geopandas as gpd

import folium
from folium import Choropleth, Circle, Marker
from folium.plugins import HeatMap

def embed_map(m, file_name):
    from IPython.display import IFrame
    m.save(file_name)
    return IFrame(file_name, width='100%', height='500px')

plate_boundaries = gpd.read_file("../input/geospatial-learn-course-data/Plate_Boundaries/Plate_Boundaries/Plate_Boundaries.shp")
plate_boundaries['coordinates'] = plate_boundaries.apply(lambda x: [(b,a) for (a,b) in list(x.geometry.coords)], axis='columns')
plate_boundaries.drop('geometry', axis=1, inplace=True)

# Load the earthquake data set
earthquakes = pd.read_csv("../input/geospatial-learn-course-data/earthquakes1970-2014.csv", parse_dates=["DateTime"])
earthquakes.head(10)
earthquakes.to_csv("earthquakes.csv")

# Creation of a base map with plate boundaries
m_1 = folium.Map(location=[35,136], tiles='cartodbpositron', zoom_start=5)
for i in range(len(plate_boundaries)):
    folium.PolyLine(locations=plate_boundaries.coordinates.iloc[i], weight=2, color='red').add_to(m_1)

# Adding a heatmap to the map
HeatMap(data=earthquakes[['Latitude', 'Longitude']], radius=15).add_to(m_1)


# Showing the map
embed_map(m_1, 'q_1.html')

# Replication a base map with plate boundaries
m_2 = folium.Map(location=[35,136], tiles='cartodbpositron', zoom_start=5)
for i in range(len(plate_boundaries)):
    folium.PolyLine(locations=plate_boundaries.coordinates.iloc[i], weight=2, color='red').add_to(m_2)
    
# Adding a map to visualize earthquake depth
def color_producer(val):
    if val <= 20:
        return 'darkred'
    else:
        return 'forestgreen'

# Adding a bubble map to the base map
for i in range(0,len(earthquakes)):
    Circle(
        location=[earthquakes.iloc[i]['Latitude'], earthquakes.iloc[i]['Longitude']],
        radius=20,
        color=color_producer(earthquakes.iloc[i]['Depth'])).add_to(m_2)
 

# View the map
embed_map(m_2, 'q_2.html')

# GeoDataFrame with prefecture boundaries
prefectures = gpd.read_file("../input/geospatial-learn-course-data/japan-prefecture-boundaries/japan-prefecture-boundaries/japan-prefecture-boundaries.shp")
prefectures.set_index('prefecture', inplace=True)
prefectures.head(10)

# DataFrame containing population of each prefecture
population = pd.read_csv("../input/geospatial-learn-course-data/japan-prefecture-population.csv")
population.set_index('prefecture', inplace=True)

# Calculating area (in square kilometers) of each prefecture
area_sqkm = pd.Series(prefectures.geometry.to_crs(epsg=32654).area / 10**6, name='area_sqkm')
stats = population.join(area_sqkm)

# Adding density (per square kilometer) of each prefecture
stats['density'] = stats["population"] / stats["area_sqkm"]
print(stats['density'])

# Creation of  a base map
m_3 = folium.Map(location=[35,136], tiles='cartodbpositron', zoom_start=5)

# A choropleth map to visualize population density
Choropleth(geo_data=prefectures.__geo_interface__, 
           data=stats['density'], 
           key_on="feature.id", 
           fill_color='YlGnBu', 
           legend_name='Japan High Population Density Areas'
          ).add_to(m_3)


# View the map
embed_map(m_3, 'q_3.html')

# Creation of  a base map
m_4 = folium.Map(location=[35,136], tiles='cartodbpositron', zoom_start=5)


Choropleth(geo_data=prefectures.__geo_interface__, 
           data=stats['density'], 
           key_on="feature.id", 
           fill_color='YlGnBu', 
           legend_name='Japan High Population Density Areas w/ High-Magnitude Earthquakes'
          ).add_to(m_4)

def color_producer(val):
    if val <= 20:
        return 'darkred'
    else:
        return 'forestgreen'

# Add a bubble map to the base map
for i in range(0,len(earthquakes)):
    Circle(
        location=[earthquakes.iloc[i]['Latitude'], earthquakes.iloc[i]['Longitude']],
        radius=20,
        color=color_producer(earthquakes.iloc[i]['Depth'])).add_to(m_4)
 


# View the map
embed_map(m_4, 'q_4.html')