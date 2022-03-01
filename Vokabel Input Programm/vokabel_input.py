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

def show_generals():
    screen.fill(background_colour[colour_mode])
    if colour_mode == 0: screen.blit(switch_to_light,(680, 680))
    if colour_mode == 1: screen.blit(switch_to_dark,(680, 680))
    if mouse_x > 680 and mouse_x < 730 and mouse_y > 680 and mouse_y < 730: screen.blit(button_hovered,(680, 680))

def input_box(Nummer, Inhalt, Eingabe, posX, posY):

    if Eingabe == '':
        input_graphic = general_font.render(Inhalt, True, font_colour[colour_mode])
    else:
        input_graphic = general_font.render(Eingabe, True, font_colour[colour_mode])
    screen.blit(input_graphic,(posX + 15, posY + 10))
    width, height = input_graphic.get_rect().size

    active = False
    if buttons_pressed[0]:
        if mouse_x >= posX and mouse_x <= posX + width + 30 and mouse_y >= posY and mouse_y <= posY + 50:
            active = True

    if active:
        pygame.draw.rect(screen, active_colour[colour_mode], pygame.Rect(posX, posY, width + 30, 50),  2)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    input = input[:-1]
                else:
                    Eingabe += event.unicode
    else:
        pygame.draw.rect(screen, inactive_colour[colour_mode], pygame.Rect(posX, posY, width + 30, 50), 2)

while True:
    mouse_x, mouse_y = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            buttons_pressed = pygame.mouse.get_pressed()
            print(buttons_pressed)
            # Colour Switch
            if buttons_pressed[0]:
                if mouse_x > 680 and mouse_x < 730 and mouse_y > 680 and mouse_y < 730:
                    colour_mode += 1
                    colour_mode = colour_mode % 2
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    show_generals()

    input_box(1, 'Stammform', '', 100, 100)

    pygame.display.flip()
    clock.tick(45)