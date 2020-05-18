import pygame


class Ship():
    """Класс для управления кораблем."""

    def __init__(self, ai_game):
        """Инициализирует корабль и задает его начальную позицию."""
        # экран присваивается атрибуту Ship, чтобы к нему можно
        # было легко обращаться во всех модулях класса
        self.screen = ai_game.screen
        # обращается к атрибуту rect позволяет разместить корабль
        # в нужной позиции экрана.
        self.screen_rect = ai_game.screen.get_rect()

        # Загружает изображение корабля и получает прямоугольник.
        self.image = pygame.image.load('alien_invasion/images/ship.bmp')
        self.rect = self.image.get_rect()
        # Каждый новый корабль появляется у нижнего края экрана.
        # self.rect.midbottom выравнивается по атрибуту midbottom
        # прямоугольника зкрана
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Рисует корабль в текущей позиции."""
        self.screen.blit(self.image, self.rect)
