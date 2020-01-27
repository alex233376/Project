import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
import game_functions as gf
def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Game Alex")
    ship = Ship(ai_settings, screen)# Создание корабля.
    bullets = Group()# Создание группы для хранения пуль.

    while True:
        # Запуск основного цикла игры.
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_screen(ai_settings, screen, ship, bullets)
run_game()
