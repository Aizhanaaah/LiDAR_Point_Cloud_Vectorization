import json

with open("config.json", "r") as f:
    config = json.load(f)

map_dimensions = config["map_dimensions"]
map_image = config["map_image"]
window_name = config["window_name"]
colors = config["colors"]

import env
import math
import pygame

environment = env.buildEnvironments(map_dimensions)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
