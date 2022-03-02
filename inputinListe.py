import pygame_textinput
import pygame
pygame.init()

# Create TextInput-object
textinput = pygame_textinput.TextInputVisualizer()

screen = pygame.display.set_mode((1000, 200))
clock = pygame.time.Clock()
textinput.value = ""
while True:
    screen.fill((225, 225, 225))

    events = pygame.event.get()

    # Feed it with events every frame
    textinput.update(events)
    # Blit its surface onto the screen
    screen.blit(textinput.surface, (10, 10))
    if textinput.value == "test":
        exit()
    for event in events:
        print(type(event))
        if event.type == pygame.QUIT:
            exit()

    pygame.display.update()
    clock.tick(30)