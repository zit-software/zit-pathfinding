import pygame
from constant.sound import winSound
from GUI import draw
from constant.dimension import *

# Init Pygame:
WIN = pygame.display.set_mode((WIDTH + 200, WIDTH))
pygame.init()
pygame.display.set_caption("Path Finding Algorithm")
pygame.init()

def reconstruct_path(came_from,start, end,board):
    pygame.mixer.Sound.play(winSound)
    current = end
    while came_from[current] != start:
        current = came_from[current]
        if current != end:
            current.make_path()

        draw(WIN,board,ROWS,WIDTH)
        pygame.time.wait(5)