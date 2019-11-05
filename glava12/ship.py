import pygame
 
class Ship():
    """Класс для управления кораблем."""
 
    def __init__(self, screen):
        """Инициализируйте корабль и установите его начальную позицию."""
        self.screen = screen
        # Загрузите изображение корабля и получите его прямоугольник.
        self.image = pygame.image.load('D:/Project/glava12/images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.bottom = self.screen_rect.bottom
        # Начните каждый новый корабль в центре нижней части экрана.
        self.rect.centerx = self.screen_rect.centerx
        

    def blitme(self):
        """Рисует корабль в текущей позиции."""
        self.screen.blit(self.image, self.rect)


