import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Новые блуждания строятся до тех пор, пока программа остается активной.
while True:
    # Построение случайного блуждания.
    rw = RandomWalk()
    rw.fill_walk()

    # Нанесение точек на диаграмму
    plt.style.use('classic')
    fig, ax = plt.subplots()
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,
               edgecolors='none', s=15)
    plt.show()

    keep_running = input("Продолжить генерацию? (y/n)")
    if keep_running == 'n':
        break
