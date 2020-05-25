import json

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

# Изучение структуры данных.
filename = 'glava16/data/eq_data_1_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)
all_eq_dicst = all_eq_data['features']
mags, lons, lats = [], [], []
for eq_dict in all_eq_dicst:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
# Нанесение данных на карту.
data = [{
    'type': 'scattergeo',
    'lon': lons,
    'lat': lats,
    'marker': {
        'size': [5*mag for mag in mags],
        'color': mags,
        'colorscale': 'Viridis',
        'reversescale': True,
        'colorbar': {'title': 'Magnitude'},
    },
}]
my_layout = Layout(title='Global Earthquakes')
fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='global_earthquakes.html')
