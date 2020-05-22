import matplotlib.pyplot as plt

x_values = list(range(1, 5001))
y_values = [x**3 for x in x_values]
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.YlOrRd, s=10)
ax.set_title("Квадрат числа", fontsize=24)
ax.set_xlabel("Значение", fontsize=14)
ax.set_ylabel("Результат квадрата", fontsize=14)
plt.show()
# Сохранение диаграммы в файл
# plt.savefig('squares_plot.png', bbox_inches='tight')
# Цветовые карты http://matplotlib.org
# раздел Examples, прокрутите содержимое до пункта Color
# и щелкните на ссылке Colormaps_reference.
