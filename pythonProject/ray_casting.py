import pygame
from settings import *
from map import world_map


def mapping(a, b):
    return (a // tile * tile, b // tile * tile)

def ray_casting(sc, player_pos, player_angle):
    ox, oy = player_pos
    xm, ym = mapping(ox, oy)
    cur_angle = player_angle - half_FOV
    for ray in range(num_rays):
        sin_a = math.sin(cur_angle)
        cos_a = math.cos(cur_angle)

        # verticals
        x, dx = (xm + tile, 1) if cos_a >= 0 else (xm, -1)
        for i in range(0, width, tile):
            depth_v = (x - ox) / cos_a
            y = oy + depth_v * sin_a
            if mapping(x + dx, y) in world_map:
                break
            x += dx * tile

        # horizontals
        y, dy = (ym + tile, 1) if sin_a >= 0 else (ym, -1)
        for i in range(0, height, tile):
            depth_h = (y - oy) / sin_a
            x = ox + depth_h * cos_a
            if mapping(x, y + dy) in world_map:
                break
            y += dy * tile

        # projections
        depth = depth_v if depth_v < depth_h else depth_h
        depth *= math.cos(player_angle - cur_angle)
        proj_height = proj_coeff / depth
        col = 255 / (1 + depth * depth * 0.00001)
        color = (col, col // 2, col // 2)
        pygame.draw.rect(sc, color, (ray * scale, half_height - proj_height // 2, scale, proj_height))
        cur_angle += delta_angle
