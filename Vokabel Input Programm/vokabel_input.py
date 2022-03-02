import pygame
import sys
import time
import os
pygame.init()
clock = pygame.time.Clock()
# For directory management
BASE_PATH = os.path.dirname(os.path.abspath(__file__))
# Set up screen
screen = pygame.display.set_mode((750, 750))
pygame.display.set_caption('Vokabel-Input')
# Colour definition
background_colour = [(47, 49, 54),(235, 237, 239)]
active_colour = [(195, 195, 195),(242, 243, 245)]
inactive_colour = [(114, 118, 125),(79, 86, 96)]
font_colour = [(219, 139, 187),(110, 141, 167)]
colour_mode = 0

general_font = pygame.font.SysFont('consolas', 36)

switch_to_light_path = os.path.join(BASE_PATH, 'graphics/toggle_to_light.png')
switch_to_light = pygame.image.load(switch_to_light_path)
switch_to_dark_path = os.path.join(BASE_PATH, 'graphics/toggle_to_dark.png')
switch_to_dark = pygame.image.load(switch_to_dark_path)
button_hovered_path = os.path.join(BASE_PATH, 'graphics/toggle_button_active.png')
button_hovered = pygame.image.load(button_hovered_path)

buttons_pressed = [False, False, False]

input_text = ''
Inputnummer = 0
def detect():
    global Inputnummer
    Inputnummer = Inputnummer+1
    if event.type == pygame.KEYDOWN:
        print(f"Detected{Inputnummer}")




def show_generals():
    screen.fill(background_colour[colour_mode])
    if colour_mode == 0: screen.blit(switch_to_light,(680, 680))
    if colour_mode == 1: screen.blit(switch_to_dark,(680, 680))
    if mouse_x > 680 and mouse_x < 730 and mouse_y > 680 and mouse_y < 730: screen.blit(button_hovered,(680, 680))

while True:
    mouse_x, mouse_y = pygame.mouse.get_pos()
    buttons_pressed == pygame.mouse.get_pressed()
    for event in pygame.event.get():

        if event.type == pygame.KEYDOWN:
            #dfgdetect()

            if event.key == pygame.K_BACKSPACE:
                input_text = input_text[:-1]
            else:
                input_text += event.unicode
                print(input_text)
        if event.type == pygame.MOUSEBUTTONDOWN:
            buttons_pressed_event = pygame.mouse.get_pressed()
            # Colour Switch
            if buttons_pressed_event[0]:
                if mouse_x > 680 and mouse_x < 730 and mouse_y > 680 and mouse_y < 730:
                    colour_mode += 1
                    colour_mode = colour_mode % 2
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    show_generals()

    pygame.display.flip()
    clock.tick(45)