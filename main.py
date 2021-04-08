"""
***************************************************
Filename: CPT Game
Description: Move the computer (Black Paddle) with the arrow keys to catch viruses (Balls). 
You are trying to get the highest score in 30 seconds. 
The big red virus will give you 1 point, the medium brown virus will give you 2 points, and the small green virus will give you 3 points. 
Author: Lee. M
Date: 03/24/2021
***************************************************
"""

# Initializing pygame + some important variables 
import pygame
from random import randint

pygame.init()

# Defining colours
Black = (0, 0, 0)
White = (255, 255, 255)
Green = (0, 255, 0)
Red = (255, 0, 0)
Blue = (0, 0, 255)
Brown = (100, 40, 0)

score = 0
total = 0

pygame.display.set_caption("Malware Game")
myfont = pygame.font.SysFont('georgia', 22)


# Making dictionaries with settings for everything.
screen = {
    "width": 1000,
    "height": 600
}

computer = {
    "width": 150,
    "height": 20,
    "x": 300,
    "y": 400,
    "velocity": 50
}

small_virus = { 
    "radius": 20, 
    "y": 30,
    "x": randint(0, screen["width"]),
    "velocity": 20
} 

med_virus = { 
    "radius": 30, 
    "y": 30,
    "x": randint(0, screen["width"]),
    "velocity": 13
} 

big_virus = { 
    "radius": 40, 
    "y": 31,
    "x": randint(0, screen["width"]),
    "velocity": 8
} 

# timer
start_ticks = pygame.time.get_ticks() 
start_ticks = True


# Launching the window, setting it to the dimensions of the `display` dictionary.
win = pygame.display.set_mode((screen["width"], screen["height"]))

# The Main game loop
while True:
    pygame.time.delay(130)
    win.fill((255, 255, 255))
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        computer["x"] -= computer["velocity"]

    if keys[pygame.K_RIGHT]:
        computer["x"] += computer["velocity"]

    if keys[pygame.K_UP]:
        computer["y"] -= computer["velocity"]

    if keys[pygame.K_DOWN]:
        computer["y"] += computer["velocity"]

    if small_virus["y"] + small_virus["radius"] >= computer["y"]:
        if small_virus["x"] > computer["x"] and small_virus["x"] < computer["x"] + computer["width"]:
            score += 3
        total += 3
        small_virus["y"] = small_virus["radius"]
        small_virus["x"] = randint(0, screen["width"])

    small_virus["y"] += small_virus["velocity"]

    if med_virus["y"] + med_virus["radius"] >= computer["y"]:
       if med_virus["x"] > computer["x"] and med_virus["x"] < computer["x"] + computer["width"]:
            score += 2
       total += 2
       med_virus["y"] = med_virus["radius"]
       med_virus["x"] = randint(0, screen["width"])

    med_virus["y"] += med_virus["velocity"]

    if big_virus["y"] + big_virus["radius"] >= computer["y"]:
        if big_virus["x"] > computer["x"] and big_virus["x"] < computer["x"] + computer["width"]:
            score += 1
        total += 0
        big_virus["y"] = big_virus["radius"]
        big_virus["x"] = randint(0, screen["width"])

    big_virus["y"] += big_virus["velocity"]

    pygame.draw.circle(win, (0, 255, 0), (small_virus["x"], small_virus["y"]), small_virus["radius"])

    pygame.draw.circle(win, (100, 40, 0), (med_virus["x"], med_virus["y"]), med_virus["radius"])

    pygame.draw.circle(win, (255, 0, 0), (big_virus["x"], big_virus["y"]), big_virus["radius"])

    pygame.draw.rect(win, (0, 0, 0), (computer["x"], computer["y"], computer["width"], computer["height"]))


    textsurface = myfont.render("score: {0}/{1}".format(score, total), False, (0, 0, 0))
    win.blit(textsurface, (10, 10))

    # setting a timer for the game to end which is 30 seconds
    seconds = (pygame.time.get_ticks()-start_ticks)/1000 
    if seconds > 30:
      break
    
    pygame.display.update()

pygame.quit()

   
