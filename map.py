import folium
import pandas
# create data object
data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
Elev = list(data["ELEV"])


def color_producer(elevation):
    if elevation < 1000:
        return "blue"
    elif 1000 <= elevation < 3000:
        return "orange"
    else:
        return "red"


html_elev = """<h4>Volcano information:</h4>
Elevation: %s m
"""
map = folium.Map(location=[38.58, -99.99],
                 zoom_start=5, tiles="Stamen Terrain")
fg = folium.FeatureGroup(name="my app")
# create multiple markers
for lt, ln, el in zip(lat, lon, Elev):
    iframe = folium.IFrame(html=html_elev % str(el), width=180, height=90)
    fg.add_child(folium.Marker(
        location=[lt, ln], popup=folium.Popup(iframe), icon=folium.Icon(color=color_producer(el))))
map.add_child(fg)
map.save("map1.html")
