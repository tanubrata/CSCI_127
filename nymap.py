#Name- Tanubrata Dey
#Date- 15 April 2018
#This program prints:NYC Map


import folium

mapCUNY = folium.Map(location=[40.75, -74.125], zoom_start=10)

folium.Marker(location = [40.768731, -73.964915], popup = "Hunter College").add_to(mapCUNY)

mapCUNY.save(outfile='nycMap.html')
