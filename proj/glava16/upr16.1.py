import csv
from matplotlib import pyplot as plt

filename = 'glava16/data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    osadki = []  # создаем список под осадки
    for row in reader:
        osadok = float(row[3])  # Сохраняем значения осадков
        osadki.append(osadok)
    # Нанесение данных на диаграмму.
    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    ax.plot(osadki, c='blue')
    plt.title("", fontsize=24)
    plt.xlabel('', fontsize=16)
    plt.ylabel("Количество осадков", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)
    plt.show()
