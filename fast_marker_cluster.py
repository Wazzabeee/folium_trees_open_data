import pandas as pd
import folium
from folium.plugins import FastMarkerCluster
import time

df = pd.read_csv('data/20190318-referentiel-arbre-namr.csv')

france_map = folium.Map(location=[46.603354, 1.888334], zoom_start=6)

start_time = time.time()

callback = """
            function (row) {
                var icon = L.AwesomeMarkers.icon({icon: 'glyphicon-tree-deciduous', markerColor: 'green'});
                    var marker = L.marker(new L.LatLng(row[0], row[1]));
                    marker.setIcon(icon);
                    
                    var popupContent = '<b>' + row[2] + '</b>';
                    marker.bindPopup(popupContent);
                    
                    return marker;
                };"""

france_map.add_child(FastMarkerCluster(data=df[['y', 'x', 'genre_latin']].values.tolist(), callback=callback))

france_map.save('urban_trees_map.html')

end_time = time.time()
execution_time_method = end_time - start_time

print("\nMethod 5: FastMarkerCluster")
print(f"Markers added: {len(df)}")
print(f"Execution time: {execution_time_method:.2f} seconds")
