import pandas as pd
import folium
from folium.plugins import MarkerCluster, FastMarkerCluster
import time

df = pd.read_csv('data/sample.csv')

france_map_1 = folium.Map(location=[46.603354, 1.888334], zoom_start=6)
france_map_2 = folium.Map(location=[46.603354, 1.888334], zoom_start=6)
france_map_3 = folium.Map(location=[46.603354, 1.888334], zoom_start=6)
france_map_4 = folium.Map(location=[46.603354, 1.888334], zoom_start=6)
france_map_5 = folium.Map(location=[46.603354, 1.888334], zoom_start=6)

marker_cluster_1 = MarkerCluster().add_to(france_map_1)
marker_cluster_2 = MarkerCluster().add_to(france_map_2)
marker_cluster_3 = MarkerCluster().add_to(france_map_3)
marker_cluster_4 = MarkerCluster().add_to(france_map_4)

# Method 1: Iterating over rows of the DataFrame
start_time = time.time()
trees_added = 0

for index, row in df.iterrows():
    tree_location = [row['y'], row['x']]
    marker = folium.Marker(location=tree_location,
                           popup=row['genre_latin'],
                           icon=folium.Icon(color='green', icon="glyphicon glyphicon-tree-deciduous"))
    marker_cluster_1.add_child(marker)
    trees_added += 1

france_map_1.save('viz/urban_trees_map_1.html')

end_time = time.time()
execution_time_method1 = end_time - start_time

# Method 2: Iterating over a list of tree locations
start_time = time.time()
trees_added = 0

tree_locations = df[['y', 'x']].values.tolist()

for tree_location in tree_locations:
    marker = folium.Marker(location=tree_location)
    marker_cluster_2.add_child(marker)
    trees_added += 1

france_map_2.save('viz/urban_trees_map_2.html')

end_time = time.time()
execution_time_method2 = end_time - start_time

# Method 3: Iterating over a NumPy array of tree locations
start_time = time.time()
trees_added = 0

tree_locations_np = df[['y', 'x']].values.astype(float)

for tree_location in tree_locations_np:
    marker = folium.Marker(location=tree_location)
    marker_cluster_3.add_child(marker)
    trees_added += 1

france_map_3.save('viz/urban_trees_map_3.html')

end_time = time.time()
execution_time_method3 = end_time - start_time

# Method 4: Lambda function
start_time = time.time()

df.apply(lambda row: folium.Marker(location=[row['y'], row['x']]).add_to(marker_cluster_4), axis=1)

france_map_4.save('viz/urban_trees_map_4.html')

end_time = time.time()
execution_time_method4 = end_time - start_time

# Method 5: FastMarkerCluster
start_time = time.time()

france_map_5.add_child(FastMarkerCluster(data=df[['y', 'x']].values.tolist()))

france_map_5.save('viz/urban_trees_map_5.html')

end_time = time.time()
execution_time_method5 = end_time - start_time

print("Method 1: Iterating over rows of the DataFrame")
print(f"{trees_added} trees added in {execution_time_method1:.2f} seconds")

print("\nMethod 2: Iterating over a list of tree locations")
print(f"{trees_added} trees added in {execution_time_method2:.2f} seconds")

print("\nMethod 3: Iterating over a Numpy array of tree locations")
print(f"{trees_added} trees added in {execution_time_method3:.2f} seconds")

print("\nMethod 4: Applying a Lambda function on the DataFrame")
print(f"{trees_added} trees added in {execution_time_method4:.2f} seconds")

print("\nMethod 5: Using the class FastMarkerCluster")
print(f"{trees_added} trees added in {execution_time_method5:.2f} seconds")
