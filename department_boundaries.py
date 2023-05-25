import folium

departments = 'data/departements.geojson'
department_geojson = folium.GeoJson(departments)

france_map = folium.Map(location=[46.603354, 1.888334], zoom_start=6)

department_geojson.add_to(france_map)

# Add the Choropleth map to the base map
folium.LayerControl().add_to(france_map)

# Save the map to an HTML file
france_map.save('french_departments.html')
