import pygame
from settings import *
import math
from ray_casting import ray_casting
from map import mini_map


class Drawing:
    def __init__(self, sc, sc_map):
        self.sc = sc
        self.sc_map = sc_map
        self.font = pygame.font.SysFont('Arial', 36, bold=True)
        self.textures = {'1': pygame.image.load('img/wall.jpg').convert(),
        '2': pygame.image.load('img/wall2.jpg').convert()}

    def background(self, player_angle):
        pygame.draw.rect(self.sc, skyblue, (0, 0, width, half_height))
        pygame.draw.rect(self.sc, dark_gray, (0, half_height, width, half_height))

    def world(self, player_pos, player_angle):
        ray_casting(self.sc, player_pos, player_angle, self.textures)

    def fps(self, clock):
        display_fps = str(int(clock.get_fps()))
        render = self.font.render(display_fps, 0, red)
        self.sc.blit(render, FPS_pos)

    def mini_map(self, player):
        self.sc_map.fill(black)
        map_x, map_y = player.x // map_scale, player.y // map_scale
        pygame.draw.line(self.sc_map, yellow, (map_x, map_y), (map_x + 12 * math.cos(player.angle),
                                               map_y + 12 * math.sin(player.angle)))
        pygame.draw.circle(self.sc_map, red, (map_x, map_y), 5)
        for x, y in mini_map:
            pygame.draw.rect(self.sc_map, green, (x, y, map_tile, map_tile))

        self.sc.blit(self.sc_map, map_pos)
