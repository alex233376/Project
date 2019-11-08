import pygame
 
class Ship():
    """Класс для управления кораблем."""
 
    def __init__(self, ai_settings, screen):
        """Инициализируйте корабль и установите его начальную позицию."""
        self.screen = screen
        self.ai_settings = ai_settings
        # Загрузите изображение корабля и получите его прямоугольник.
        self.image = pygame.image.load('D:/Project/glava12/images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
        self.rect.bottom = self.screen_rect.bottom
        # Каждый новый корабль появляется у нижнего края экрана.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        self.center = float(self.rect.centerx)# Сохранение вещественной координаты центра корабля.
        # Флаг перемещения
        self.moving_right = False
        self.moving_left = False
    def update(self):
        """Обновляет позицию корабля с учетом флага."""
        # Обновляется атрибут center, не rect.
        if self.moving_right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left:
            self.center -= self.ai_settings.ship_speed_factor
        self.rect.centerx = self.center# Обновление атрибута rect на основании self.center.
    def blitme(self):
        """Рисует корабль в текущей позиции."""
        self.screen.blit(self.image, self.rect)


