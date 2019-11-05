import pygame
 
class Ship:
    def __init__(self, screen):
        """Инициализируйте корабль и установите его начальную позицию."""
        self.screen = screen
        # Загрузите изображение корабля и получите его прямоугольник.
        self.image = pygame.image.load('D:/Project/glava12/images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        # Начните каждый новый корабль в центре нижней части экрана.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
    def blitme(self):
        """Нарисуйте корабль в его текущем местоположении."""
        self.screen.blit(self.image, self.rect)
