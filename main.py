""" Main execution module of the game. """

import pygame

class Matrix():
    def __init__(self):
        self.values = {}
        self.create_matrix()

    def alternate(self):
        while True:
          yield 0
          yield 1
       
    def create_matrix(self):
        y = -20
        colour_change = self.alternate()
        for number in "87654321":
            colour = next(colour_change)
            x = 152
            y += 71
            for letter in "abcdefgh":
                self.values[letter + number] = (x, y, colour)
                colour = next(colour_change)
                x += 71

class Square(pygame.sprite.Sprite):
    def __init__(self, x, y, colour):
        super().__init__()       
        
        if colour == 0:
            self.image = pygame.image.load('graphics/squares/square_brown_light.png').convert()
        else:
            self.image = pygame.image.load('graphics/squares/square_brown_dark.png').convert()
        
        self.image = pygame.transform.scale(self.image, (71, 71))
        self.rect = self.image.get_rect(center = (x, y))

def draw_board():
    matrix = Matrix()
    squares = pygame.sprite.Group()
    for value in matrix.values.values():  
        x = value[0]
        y = value[1]
        colour = value[2]
        squares.add(Square(x, y, colour))

    squares.draw(screen)

pygame.init()
screen = pygame.display.set_mode((800, 600))
icon = pygame.image.load('graphics/pieces/b_king.png')
pygame.display.set_caption('Chess')
pygame.display.set_icon(icon)
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit
            exit()

    draw_board()

    pygame.display.update()
    clock.tick(60)