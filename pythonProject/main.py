import pygame
from settings import *
from player import Player
import math

pygame.init()
sc = pygame.display.set_mode((width, height))
player = Player()
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    player.movement()
    sc.fill(black)

    pygame.draw.circle(sc, green, player.pos, 12)
    pygame.draw.line(sc, red, player.pos, (player.x + width * math.cos(player.angle),
                                           player.y + height * math.sin(player.angle)))

    pygame.display.flip()
    clock.tick(FPS)
