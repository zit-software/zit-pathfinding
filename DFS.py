# DFS
from queue import LifoQueue
import pygame
from constant.sound import *
from constant.image import *
from common import  reconstruct_path, WIN
from GUI import draw

def DFS(board,start,end):
    stack = LifoQueue()
    came_from = {}
    stack.put(start)
    visited = {start}
    previous=start
    while not stack.empty():
        pygame.time.wait(200)
        pygame.mixer.Sound(swimmingSound).play()
        current = stack.get()
        if current == end:
            previous.setImage(footPrintImg)
            reconstruct_path(came_from,start,end,board)
            return True
        if previous == start:
            previous.setImage(startImg)
            current.setImage(duckImg)
        else:
            previous.setImage(footPrintImg)
            current.setImage(duckImg)
        previous = current
        if current != start:
            current.make_closed()
        for neighbour in current.neighbour:
            if neighbour not in visited:
                stack.put(neighbour)
                visited.add(neighbour)
                came_from[neighbour] = current
                if neighbour != end:
                    neighbour.make_open()

        draw(WIN,board,ROWS,WIDTH)
    return False
# END DFS