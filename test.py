import pygame
import sys
import time
clock = pygame.time.Clock()
pygame.init()

screen = pygame.display.set_mode((750, 750))
pygame.display.set_caption("Hallo")

def detect():
    if event.type == pygame.KEYDOWN:
        print("Detected")

while True:
    clock.tick(45)
    for event in pygame.event.get():
        detect()
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()