import pygame
pygame.init()

class Rectangle:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.width = w
        self.height = h




class GUI: # controller
    def __init__(self):
        self.screen = pygame.display.set_mode([500, 500])
        self.screen.fill((255, 255, 255))
        pygame.display.set_caption('Frogger')


    def startup(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event == pygame.QUIT:
                    running = False

run = GUI()
run.startup()
