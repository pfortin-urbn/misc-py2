#Import Library
import folium
from folium.plugins import MarkerCluster
import pandas as pd

#Function to change colors
def color_change(elev):
    if(elev < 1000):
        return('green')
    elif(1000 <= elev <3000):
        return('orange')
    else:
        return('red')

#Load Data
data = pd.read_csv("Volcanoes_USA.txt")
lat = data['LAT']
lon = data['LON']
name = data['NAME']
elevation = data['ELEV']

#Create base map
map = folium.Map(location=[38, -102], zoom_start=5, tiles="Mapbox bright")

#Create Cluster
marker_cluster = MarkerCluster().add_to(map)

#Plot Volcanoes and their elevation
for lat, lon, name, elevation in zip(lat, lon, name, elevation):
    popup_txt = "Mt. "+ str(name) + "<br>" + str(elevation)+" m"
    #folium.Marker(location=[lat, lon], popup=popup_txt, icon=folium.Icon(color=color_change(elevation))).add_to(map)
    folium.CircleMarker(location=[lat, lon], radius = 9, popup=popup_txt, fill_color=color_change(elevation), color="gray", fill_opacity = 0.9).add_to(marker_cluster)

#Save the map
map.save("map1.html")
