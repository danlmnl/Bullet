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

    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (255, 0, 0), redcircle, redrad)
    pygame.draw.circle(screen, (0, 255, 255), blcircle, bluerad)
    if bullet is not None:
        pygame.draw.circle(screen, (0, 0, 255), bullet, bulrad)
    text = font.render("Пушка", True, (0, 0, 0))
    screen.blit(text, (size[0]/2 - 40, size[1] - normalsize))
    pygame.display.flip()
