import math


# game settings
width = 1200
height = 800
half_width = width // 2
half_height = height // 2
FPS = 60
tile = 100


# ray casting settings
FOV = math.pi / 3
half_FOV = FOV / 2
num_rays = 120
max_depth = 800
delta_angle = FOV / num_rays
dist = num_rays / (2 * math.tan(half_FOV))
proj_coeff = 4 * dist * tile
scale = width // num_rays


# player settings
player_pos = (half_width, half_height)
player_angle = 0
player_speed = 2

# colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (220, 0, 0)
green = (0, 220, 0)
blue = (0, 0, 220)
dark_gray = (110, 110, 110)
purple = (120, 0, 120)
skyblue = (0, 186, 255)
