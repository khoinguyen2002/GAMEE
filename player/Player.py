from game_object import GameObject
import pygame
from frame_counter import FrameCounter
class Player(GameObject):
    # 1. Create constructor (properties)
    def __init__(self, x, y, input_manager):
        GameObject.__init__(self, x, y)
        self.image = pygame.image.load('')
        self.input_manager = input_manager
        self.shoot_lock = False
        self.counter = FrameCounter(30)

    # 2. Describe action / method / behavior
    def update(self):
        GameObject.update(self)
        self.move()
        self.shoot()

    def move(self):
        dx = 0
        dy = 0

        if self.input_manager.right_pressed:
            dx += 3
        if self.input_manager.left_pressed:
            dx -= 3
        if self.input_manager.down_pressed:
            dy += 3
        if self.input_manager.up_pressed:
            dy -= 3

        self.x += dx
        self.y += dy



