import matplotlib.pyplot as plt

x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 9, 16, 25]

plt.style.use('seaborn-darkgrid')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=100)  # Передаём точки
# ax.plot(x_values, y_values, linewidth=3)
# Назначение заголовка диаграммы и меток осей
ax.set_title("Квадрат числа", fontsize=24)
ax.set_xlabel("Значение", fontsize=14)
ax.set_ylabel("Результат квадрата", fontsize=14)

# Назначение размера шрифта делений на осях.
ax.tick_params(axis='both', which='major')

plt.show()
