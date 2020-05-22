"""Строить списки вручную неэффективно, особенно при большом объеме данных.
Вместо того чтобы передавать данные в виде списка, мы воспользуемся циклом
Python, который выполнит вычисления за нас. Вот как выглядит такой цикл для
1000 точек:"""
import matplotlib.pyplot as plt

x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)
# Назначение заголовка диаграммы и меток осей
ax.set_title("Квадрат числа", fontsize=24)
ax.set_xlabel("Значение", fontsize=14)
ax.set_ylabel("Результат квадрата", fontsize=14)
# Назначение диапазона для каждой оси.
ax.axis([0, 1100, 0, 1100000])

plt.show()
