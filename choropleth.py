import pandas as pd
import folium

departments = 'data/departements.geojson'
department_geojson = folium.GeoJson(departments)

geojson_file = 'data/20190318-referentiel-arbre-namr.csv'
df = pd.read_csv(geojson_file)
df['code_dept'] = df['code_dept'].astype(str).str.zfill(2)

tree_count = df.groupby('code_dept').size().reset_index(name='Tree_Count')
tree_count['norm_count'] = (tree_count['Tree_Count'] - tree_count['Tree_Count'].min()) / (tree_count['Tree_Count'].max()- tree_count['Tree_Count'].min())

# Create a base map
france_map = folium.Map(location=[46.603354, 1.888334], zoom_start=6)

# Create a Choropleth map using the number of trees per department
choropleth = folium.Choropleth(
    geo_data=departments,
    name='choropleth',
    data=tree_count,
    columns=['code_dept', 'norm_count'],
    key_on='feature.properties.code',
    fill_color='YlGnBu',
    nan_fill_color="White",
    highlight=True,
    line_color='black',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='Tree Density per Department'
).add_to(france_map)

# add labels indicating the name of the community
style_function = "font-size: 15px; font-weight: bold"
choropleth.geojson.add_child(
    folium.features.GeoJsonTooltip(['nom'], style=style_function, labels=False))

# Add the Choropleth map to the base map
folium.LayerControl().add_to(france_map)

# Save the map to an HTML file
france_map.save('tree_density_choropleth_map.html')
