import pygame
import sys

pygame.init()
win = pygame.display.set_mode((500, 500), pygame.FULLSCREEN)
pygame.display.set_caption("Raketa")

x = 230
y = 230
width = 40
height = 60
speed = 5

while True:
    pygame.time.delay(10)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > 5:
        x -= speed
    if keys[pygame.K_RIGHT] and x < 500 - width - 5:
        x += speed
    if keys[pygame.K_UP] and y > 5:
        y -= speed
    if keys[pygame.K_DOWN] and y < 500 - height - 5:
        y += speed
    win.fill((0, 0, 0))

    pygame.draw.rect(win, (0, 0, 255), (x, y, width, height))
    pygame.display.update()
