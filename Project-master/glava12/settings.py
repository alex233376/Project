class Settings:
    """Класс для хранения всех настроек для Alien Invasion."""

    def __init__(self):
        """Инициализировать настройки игры."""
        # Настройки экрана
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Настройки корабля
        self.ship_speed_factor = 1.5