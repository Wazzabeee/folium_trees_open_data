import pandas as pd
import folium
from folium.plugins import HeatMap
import time

df = pd.read_csv('data/20190318-referentiel-arbre-namr.csv')

france_map = folium.Map(location=[46.603354, 1.888334], zoom_start=6)

start_time = time.time()

# Create a HeatMap layer using KDE to visualize tree density
heat_data = df[['y', 'x']].values.tolist()
HeatMap(heat_data, radius=15).add_to(france_map)

france_map.save('viz/basic_heat_map.html')

end_time = time.time()
execution_time_method = end_time - start_time

print("\nHeat Map")
print(f"Tree count: {len(df)}")
print(f"Execution time: {execution_time_method:.2f} seconds")
