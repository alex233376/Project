import csv
from matplotlib import pyplot as plt
filename = 'glava16\\data\\sitka_weather_07-2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    # Чтение максимальных температур
    highs = []
    for row in reader:
        high = int(row[5])
        highs.append(high)
print(highs)
