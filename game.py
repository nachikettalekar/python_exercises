# Importing the libraries

import sys
import time
import random
 
# Initializing the pygame
pygame.init()

# Frames per second
clock = pygame.time.Clock()


# Function to draw
def draw_floor():
    screen.blit(floor_img, (floor_x, 520))
    screen.blit(floor_img, (floor_x + 448, 520))


# Function to create pipes
def create_pipes():
    pipe_y = random.choice(pipe_height)
    top_pipe = pipe_img.get_rect(midbottom=(467, pipe_y - 300))
    bottom_pipe = pipe_img.get_rect(midtop=(467, pipe_y))
    return top_pipe, bottom_pipe
# Importing the libraries
import pygame
import sys
import time
import random

# Initializing the pygame
pygame.init()

# Frames per second
clock = pygame.time.Clock()


# Function to draw
def draw_floor():
    screen.blit(floor_img, (floor_x, 520))
    screen.blit(floor_img, (floor_x + 448, 520))


# Function to create pipes
def create_pipes():
    pipe_y = random.choice(pipe_height)
    top_pipe = pipe_img.get_rect(midbottom=(467, pipe_y - 300))
    bottom_pipe = pipe_img.get_rect(midtop=(467, pipe_y))
    return top_pipe, bottom_pipe





