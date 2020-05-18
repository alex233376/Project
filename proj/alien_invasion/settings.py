class Settings():
    """Класс для хранения всех настроек игры Alien Invasion."""
    def __init__(self):
        """Инициализирует настройки игры."""
        # Параметры экрана
        self.screen_width = 1400
        self.screen_height = 900
        self.bg_color = (198, 166, 100)
        # Настройки корабля
        self.ship_speed = 1.5
