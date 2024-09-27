import pygame
from settings import *
from player import Player
import math
from map import world_map
from ray_casting import ray_casting

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
    pygame.draw.rect(sc, blue, (0, 0, width, half_height))
    pygame.draw.rect(sc, dark_gray, (0, half_height, width, half_height))

    ray_casting(sc, player.pos, player.angle)

    # pygame.draw.circle(sc, green, (player.x, player.y), 12)
    # pygame.draw.line(sc, red, player.pos,(player.x + width * math.cos(player.angle),
    #                                                player.y + height * math.sin (player.angle)))
    # for x, y in world_map:
    #     pygame.draw.rect(sc, dark_gray, (x, y, tile, tile), 2)
    pygame.display.flip()
    clock.tick(FPS)
