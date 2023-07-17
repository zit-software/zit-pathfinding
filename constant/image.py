import pygame
from constant.dimension import *
duckImg = pygame.transform.scale(pygame.image.load("./image/Duck.png"), (WIDTH // ROWS
                                                                         , WIDTH // ROWS))
finishLineImg = pygame.transform.scale(pygame.image.load("./image/FinishLine.png"), (WIDTH // ROWS
                                                                                     , WIDTH // ROWS))
grassImg = pygame.transform.scale(pygame.image.load("./image/Grass.png"), (WIDTH // ROWS
                                                                           , WIDTH // ROWS))
waterImg = pygame.transform.scale(pygame.image.load("./image/Water.png"), (WIDTH // ROWS
                                                                           , WIDTH // ROWS))
landImg = pygame.transform.scale(pygame.image.load("./image/Land.png"), (WIDTH // ROWS
                                                                         , WIDTH // ROWS))
flagImg = pygame.transform.scale(pygame.image.load("./image/Flag.png"), (WIDTH // ROWS
                                                                         , WIDTH // ROWS))
stopImg = pygame.transform.scale(pygame.image.load("./image/Stop.png"), (WIDTH // ROWS
                                                                         , WIDTH // ROWS))
startImg = pygame.transform.scale(pygame.image.load("./image/start.jpg"), (WIDTH // ROWS
                                                                           , WIDTH // ROWS))
footPrintImg = pygame.transform.scale(pygame.image.load("./image/Footprint.png"), (WIDTH // ROWS
                                                                                   , WIDTH // ROWS))