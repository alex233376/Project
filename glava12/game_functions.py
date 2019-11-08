import sys
import pygame
def check_events(ship):
    """Обрабатывает нажатия клавиш и события мыши."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:#проверка нажатия клавиши со стрелками
            if event.key == pygame.K_RIGHT:#кнопка нажата двигаемся в право
                ship.moving_right = True
            elif event.key == pygame.K_LEFT:#кнопка нажата двигаемся в лево
                ship.moving_left = True
        elif event.type == pygame.KEYUP:# проверка что кнопка отпущенна
            if event.key == pygame.K_RIGHT:#кнопка отпущенна остановились
                ship.moving_right = False
            elif event.key == pygame.K_LEFT:#кнопка отпущенна остановились
                ship.moving_left = False


def update_screen(ai_settings, screen, ship):
    """Обновляет изображения на экране и отображает новый экран."""
    # При каждом проходе цикла перерисовывается экран.
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    # Отображение последнего прорисованного экрана.
    pygame.display.flip()