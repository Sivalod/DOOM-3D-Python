import pygame
from settings import *
from player import Player
import math
from map import world_map
from ray_casting import ray_casting
from drawing import Drawing

pygame.init()
sc = pygame.display.set_mode((width, height))
player = Player()
clock = pygame.time.Clock()
drawing = Drawing(sc)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    player.movement()
    sc.fill(black)

    drawing.background()
    drawing.world(player.pos, player.angle)
    drawing.fps(clock)
    # pygame.draw.circle(sc, green, (player.x, player.y), 12)
    # pygame.draw.line(sc, red, player.pos,(player.x + width * math.cos(player.angle),
    #                                                player.y + height * math.sin (player.angle)))
    # for x, y in world_map:
    #     pygame.draw.rect(sc, dark_gray, (x, y, tile, tile), 2)
    pygame.display.flip()
    clock.tick(FPS)
