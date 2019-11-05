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
        # Каждый новый корабль появляется у нижнего края экрана.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        # Флаг перемещения
        self.moving_right = False
    def update(self):
        """Обновляет позицию корабля с учетом флага."""
        if self.moving_right:
            self.rect.centerx += 1
    def blitme(self):
        """Рисует корабль в текущей позиции."""
        self.screen.blit(self.image, self.rect)


