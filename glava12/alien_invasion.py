import sys

import pygame

from settings import Settings
from ship import Ship


class AlienInvasion:
    """Общий класс для управления игровыми активами и поведением."""

    def __init__(self):
        """Инициализируйте игру и создайте игровые ресурсы."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

    def run_game(self):
        """Запустите основной цикл игры."""
        while True:
            #Следите за событиями клавиатуры и мыши.
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            # Перерисовывайте экран при каждом прохождении цикла.
            self.screen.fill(self.settings.bg_color)
            self.ship.blitme()

            # Сделайте последний нарисованный экран видимым.
            pygame.display.flip()


if __name__ == '__main__':
    # Сделайте экземпляр игры и запустите игру.
    ai = AlienInvasion()
    ai.run_game()
