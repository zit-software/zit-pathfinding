import pygame
from constant.color import *
from constant.dimension import *


class Button:
    def __init__(self, color, x, y,width, height,text = ''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self,win, outline = None):
        if outline:  # Draw ouline
            pygame.draw.rect(win, outline, (self.x - 2,self.y - 2 ,self.width + 4, self.height + 4),0)
        pygame.draw.rect(win, self.color,(self.x, self.y, self.width,self.height), 0)
        if self.text != "":
            font = pygame.font.SysFont('comicsans',20)
            text = font.render(self.text,True,BLACK)
            win.blit(text, (self.x + (self.width/2 - text.get_width()/ 2), self.y + (self.height / 2 - text.get_height() / 2)))

    def is_over(self,pos):
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True

        return False


# MAKING BUTTONS:
y = 50
gap = 70
height = 40
A_Star_Button = Button(YELLOW, WIDTH + 40, y, 120, height, "A*")
y += gap
Dijkstra_button = Button(YELLOW, WIDTH + 40, y, 120, height, "DIJKSTRA")
y += gap
BFS_Button = Button(YELLOW, WIDTH + 40, y, 120, height, "BFS")
y += gap
DFS_Button = Button(YELLOW, WIDTH + 40, y, 120, height, "DFS")
y += gap
Reset_Button = Button(LIGHTORANGE, WIDTH + 40, y, 120, height, "Reset")
y += gap
Clear_Button = Button(LIGHTORANGE, WIDTH + 40, y, 120, height, "Clear")
y += gap
Random_Button = Button(LIGHTORANGE, WIDTH + 40, y, 120, height, "Random")
y += gap
Exit_Button = Button(LIGHTORANGE, WIDTH + 40, y, 120, height, "Exit")
# END MAKING BUTTONS




def draw_grid(win, rows, total_width):
    width = total_width // rows
    for i in range(rows):
        pygame.draw.line(win,BLACK,(0,i * width),(total_width, i * width))
        for j in range(rows + 1):
            pygame.draw.line(win, BLACK, (j * width , 0), (j * width ,total_width))


def draw(win, board, rows, total_width):
    win.fill(WHITE)
    # Draw menu
    pygame.draw.rect(win,WHITE,(WIDTH,0,200,WIDTH),0)

    A_Star_Button.draw(win, BLACK)
    Reset_Button.draw(win, BLACK)
    BFS_Button.draw(win, BLACK)
    Exit_Button.draw(win, BLACK)
    DFS_Button.draw(win, BLACK)
    Clear_Button.draw(win, BLACK)
    Random_Button.draw(win,BLACK)
    Dijkstra_button.draw(win,BLACK)


    for row in board:
        for cell in row:
            cell.draw(win)
    draw_grid(win, rows, total_width)

    pygame.display.update()
