import pygame
import sys
import random

pygame.init()
size = [1000, 800]
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
r = random
font = pygame.font.Font(None, 36)
normalsize = 30
redrad, bluerad, bulrad = 30, 60, 15
blcircle = pygame.Vector2(size[0] / 2, size[1])
redcircle = pygame.Vector2(r.randint(normalsize, size[0]-normalsize), r.randint(normalsize, size[1]-normalsize))
coef_speed = 7
forback = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)
cyan = (0, 255, 255)

bullet = None
speed = None

while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN and bullet is None:
            bullet = blcircle.copy()
            speed = (redcircle - blcircle).normalize()*coef_speed
    if bullet is not None:
        bullet += speed
        if bullet.distance_to(redcircle) <= redrad:
            bullet = None
            redcircle = pygame.Vector2(r.randint(normalsize, size[0]-normalsize), r.randint(normalsize, size[1]-normalsize))

    screen.fill(forback)
    pygame.draw.circle(screen, red, redcircle, redrad)
    pygame.draw.circle(screen, cyan, blcircle, bluerad)
    if bullet is not None:
        pygame.draw.circle(screen, blue, bullet, bulrad)
    text = font.render("Пушка", True, (0, 0, 0))
    screen.blit(text, (size[0]/2 - 40, size[1] - normalsize))
    pygame.display.flip()
