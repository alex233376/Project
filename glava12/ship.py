import pygame
 
class Ship:
    """Класс для управления кораблем."""
 
    def __init__(self, ai_game):
        """Инициализируйте корабль и установите его начальную позицию."""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        # Загрузите изображение корабля и получите его прямоугольник.
        self.image = pygame.image.load('D:/Project/glava12/images/ship.bmp')
        self.rect = self.image.get_rect()

        # Начните каждый новый корабль в центре нижней части экрана.
        self.rect.midbottom = self.screen_rect.midbottom

    def blitme(self):
        """Нарисуйте корабль в его текущем местоположении."""
        self.screen.blit(self.image, self.rect)
