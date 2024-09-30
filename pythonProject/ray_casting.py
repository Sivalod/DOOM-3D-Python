import pygame
from settings import *
from map import world_map


def ray_casting(sc, player_pos, player_angle):
    cur_angle = player_angle - half_FOV
    x0, y0 = player_pos
    for ray in range(num_rays):
        sin_a = math.sin(cur_angle)
        cos_a = math.cos(cur_angle)
        for depth in range(max_depth):
            x = x0 + depth * cos_a
            y = y0 + depth * sin_a
            if (x // tile * tile, y // tile * tile) in world_map:
                depth *= math.cos(player_angle - cur_angle)
                proj_height = proj_coeff / depth
                col = 255 / (1 + depth * depth * 0.00001)
                color = (col, col // 2, col // 2)
                pygame.draw.rect(sc, color, (ray * scale, half_height - proj_height // 2, scale, proj_height))
                break
        cur_angle += delta_angle
