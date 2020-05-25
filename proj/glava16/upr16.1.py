import csv
from datetime import datetime

from matplotlib import pyplot as plt

filename = 'glava16/data/sitka_weather_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    dates, osadki = [], []  # создаем список под осадки
    for row in reader:
        current_date = datetime.strptime(row[2], "%Y-%m-%d")
        osadok = float(row[3])  # Сохраняем значения осадков
        dates.append(current_date)
        osadki.append(osadok)
    # Нанесение данных на диаграмму.
    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    ax.plot(dates, osadki, c='blue')
    plt.title("", fontsize=24)
    plt.xlabel('', fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Количество осадков", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)
    plt.show()
