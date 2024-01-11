import pygame
import random
import sys

# Stores the value the x and y values will be increased by to make the scaling factor 4
width = 2

# Will store the number of R, G, or B pixels that will be randomly positioned in an area
numr = 0
numb = 0
numg = 0

# Gets the source image from the user, from the command line
srcimg = pygame.image.load(sys.argv[1])

# Gets the size of the source image's window
(w, h) = srcimg.get_size()

# Makes the window 2 times the size of the source image window
win = pygame.display.set_mode((w*width, h*width))

# Goes through every pixel
for y in range (h):
    for x in range (w):
        
        # Collects the needed R,G and B values for the given pixel
        (r, g, b, _) = srcimg.get_at((x, y))

        # Floor divides the values to determine the number of R, G, and B pixels needed
        numr = r // 50
        numb = b // 50
        numg = g // 50

        # Draws the calculated amount of R, G and B rectangles, randomly throughout the given area
        for red in range (numr):
            pygame.draw.rect(win, (255, 0, 0),(x * width + random.randint(0, 4), y * width + random.randint(0, 4), 1, 1))

        for green in range (numg):
            pygame.draw.rect(win, (0, 255, 0),(x * width + random.randint(0, 4), y * width + random.randint(0, 4), 1, 1))

        for blue in range (numb):
            pygame.draw.rect(win, (0, 0, 255),(x * width + random.randint(0, 4), y * width + random.randint(0, 4), 1, 1))

# Displays the window        
pygame.display.update()

# Keeps the window open until the user exits the window
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
