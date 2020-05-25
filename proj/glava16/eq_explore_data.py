import json
# Изучение структуры данных.
filename = 'glava16/data/eq_data_1_day_m1.json'
with open(filename) as f:
    all_eq_data = json.load(f)
all_eq_dicst = all_eq_data['features']
mags = []
for eq_dict in all_eq_dicst:
    mag = eq_dict['properties']['mag']
    mags.append(mag)
print(mags[:10])
