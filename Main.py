import pygame
import game_object
from input import input_manager
from player import Player
BG = (255, 255, 0)

# 1. Init pygame
pygame.init()

# 2. Set screen
SIZE = (800,640)
canvas = pygame.display.set_mode(SIZE)

# 3. Clock
clock = pygame.time.Clock()

loop = True

# input_manager =InputManager()

player = Player(400, 580,input_manager)

game_object.add(player)

while loop:
    # 1. Event processing
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            loop = False
        else:
            input_manager.update(event)

    game_object.update()

    # 2. Draw
    canvas.fill(BG)

    game_object.render(canvas)
    pygame.display.set_caption('đoán xem')


    # 3. Flip
    pygame.display.flip()
    clock.tick(60)

