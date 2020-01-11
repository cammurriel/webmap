import folium,io
import pandas

#opening the file Volcanoes.txt which has the lat and long for the volcanoes
data=pandas.read_csv("Volcanoes.txt")
#reading from the file world.json
data_json = io.open("world.json",'r',encoding='utf-8-sig').read()
#latitude coordinates recieved from "Volcanoes.txt" and made a list

latitude=list(data["LAT"])

#longitude coordinates recieved from "Volcanoes.txt" and made a list

longitude=list(data["LON"])
#elevation  recieved from "Volcanoes.txt" and made a list

elevation=list(data["ELEV"])
#name recieved from "Volcanoes.txt" and made a list

name= list(data["NAME"])
#function used for the color of CircleMarker in the for loop
def color_marker(elevation):
    if elevation <1000:
        return 'green'
    elif elevation <=1000 or elevation <3000:
        return 'orange'
    else:
        return'red'

#creating a FeatureGroup for the volcanoes part of the map
fgv=folium.FeatureGroup(name="Volcanoes")

for lat,long,nme,elev in zip(latitude,longitude,name,elevation):
    #adds a marker to USA portion of map and creates circle markers
    fgv.add_child(folium.CircleMarker(location=[lat,long],radius=6,popup= nme +": \n" + (str(elev))+ " m"
    ,color_points=color_marker(elev), color=color_marker(elev),fill=True, fill_opacity=0.7))


map=folium.Map(location=[38.58,-99.09],zoom_start=6,tiles="Stamen Terrain")
#creating a FeatureGroup for the population part of the map

fgp=folium.FeatureGroup(name="Population")

#creates GeoJson object, world.py is the GeoJson data that we are reading from
#sets the color of the map to certain color based upon population size
fgp.add_child(folium.GeoJson(data=data_json,style_function=lambda x: {'fillColor':'yellow' if x['properties']
['POP2005'] < 10000000
else 'green' if 10000000 <= x['properties']['POP2005'] < 20000000 else
'red' }))
map.add_child(fgv)
map.add_child(fgp)
#layer control is used to turn on or off the FeatureGroup for "Volcanoes" and "Population"
map.add_child(folium.LayerControl())

map.save("Map1.html")
