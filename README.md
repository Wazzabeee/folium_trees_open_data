# Folium Trees Open Data

Repository used in one of my Medium articles containing scripts for visualizing an open data dataset with more than 2 million GPS positions of trees in French urban areas.

The dataset containing the individual locations of trees in French urban areas is available on [datagouv.fr](https://www.data.gouv.fr/fr/datasets/arbres-en-open-data-en-france-par-namr/#resources-panel) and has been published by the company [namR](https://www.data.gouv.fr/fr/organizations/namr/) based on the aggregation of other datasets published by French municipalities under the [ODbL license](https://opendatacommons.org/licenses/odbl/summary/).

The dataset used to define the boundaries of French departments comes from the [National Institute of Geographic and Forest Information (IGN)](https://geoservices.ign.fr/adminexpress) published under the [Open Data](https://www.etalab.gouv.fr/licence-ouverte-open-licence/) license and has been converted to GEOJSON format by [Github contributors](https://github.com/gregoiredavid/france-geojson) (Updated in 2018).

This repository covers : 
- Efficient placement of custom markers with FastMakerCluster
- Heat map with a draggable legend
- Choropleth map of tree density by department

---
## Fast Marker Cluster
<img src="viz/markers.gif"/>

---
## Heat Map with Legend
<img src="viz/heatmap.gif"/>

---
## Choropleth Map
<img src="viz/choropleth.gif"/>

