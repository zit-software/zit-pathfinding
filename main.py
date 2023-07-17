import random

from constant.sound import *
from Cell import Cell
from GUI import *
from AStar import AStar
from BFS import BFS
from DFS import DFS
from Dijkstra import Dijkstra
from common import *


# BOARD UTILS:
def make_board(rows, WIDTH):
    board = []
    width = WIDTH // rows  # Width of one cell
    for i in range(rows):
        board.append([])
        for j in range(rows):
            cell = Cell(i,j,width, rows)
            board[i].append(cell)

    return board


def clear(board):
    for row in board:
        for cell in row:
            if not (cell.is_barrier() or cell.is_start() or cell.is_end()):
                cell.reset()


def show_path(board):
    for row in board:
        for cell in row:
            if not (cell.is_barrier() or cell.is_start() or cell.is_end() or cell.is_path()):
                cell.reset()


def random_obs(board):
    clear(board)
    for row in board:
        for cell in row:
            cell.make_barrier()
    width = len(board)
    height = len(board)
    for _ in range(2):
        start_x = random.randint(0, width - 1)
        start_y = random.randint(0, height - 1)
        # Depth-First Search algorithm
        stack = [(start_x, start_y)]
        while stack:
            current_x, current_y = stack[-1]

            # Find unvisited neighbors
            neighbors = []
            if current_x > 1 and board[current_y][current_x - 2].is_barrier():
                neighbors.append((current_x - 2, current_y))
            if current_x < width - 2 and board[current_y][current_x + 2].is_barrier():
                neighbors.append((current_x + 2, current_y))
            if current_y > 1 and board[current_y - 2][current_x].is_barrier():
                neighbors.append((current_x, current_y - 2))
            if current_y < height - 2 and board[current_y + 2][current_x].is_barrier():
                neighbors.append((current_x, current_y + 2))

            if neighbors:
                # Choose a random neighbor
                next_x, next_y = random.choice(neighbors)

                # Remove the wall between the current cell and the chosen neighbor
                board[(current_y + next_y) // 2][(current_x + next_x) // 2].reset()
                board[next_y][next_x].reset()

                # Move to the next cell
                stack.append((next_x, next_y))
            else:
                # Backtrack if there are no unvisited neighbors
                stack.pop()
    return board


def get_clicked_pos(pos, rows, width):
    gap = width // rows
    y, x = pos

    row = y // gap
    col = x // gap
    return row, col


# Main Function
def main():
    board = []
    board = make_board(ROWS, WIDTH)
    start = None
    end = None
    run = True
    board = random_obs(board)
    print(board)
    pygame.mixer.Sound(themeSound).play(loops=-1)
    while run:
        draw(WIN,board,ROWS,WIDTH)
        for event in pygame.event.get():
            m_pos = pygame.mouse.get_pos()
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEMOTION:  # Check motion for button
                if A_Star_Button.is_over(m_pos):
                    A_Star_Button.color = GREEN
                else:
                    A_Star_Button.color = YELLOW

                if Reset_Button.is_over(m_pos):
                    Reset_Button.color = GREEN
                else:
                    Reset_Button.color = LIGHTORANGE

                if BFS_Button.is_over(m_pos):
                    BFS_Button.color = GREEN
                else:
                    BFS_Button.color = YELLOW

                if Exit_Button.is_over(m_pos):
                    Exit_Button.color = GREEN
                else:
                    Exit_Button.color = LIGHTORANGE

                if DFS_Button.is_over(m_pos):
                    DFS_Button.color = GREEN
                else:
                    DFS_Button.color = YELLOW

                if Clear_Button.is_over(m_pos):
                    Clear_Button.color = GREEN
                else:
                    Clear_Button.color = LIGHTORANGE

                if Random_Button.is_over(m_pos):
                    Random_Button.color = GREEN
                else:
                    Random_Button.color = LIGHTORANGE

                if Dijkstra_button.is_over(m_pos):
                    Dijkstra_button.color = GREEN
                else:
                    Dijkstra_button.color = YELLOW
            if pygame.mouse.get_pressed()[0]:
                if A_Star_Button.is_over(m_pos):  # Click on button to start A* algo
                    for row in board:
                        for cell in row:
                            cell.update_neighbor(board)
                    if start and end:
                        AStar(board,start,end)
                elif Reset_Button.is_over(m_pos):  # Reset the board
                    board = make_board(ROWS,WIDTH)
                    start = None
                    end = None
                elif BFS_Button.is_over(m_pos):  # Start BFS Algo
                    for row in board:
                        for cell in row:
                            cell.update_neighbor(board)
                    if start and end:
                        BFS(board,start,end)
                elif Exit_Button.is_over(m_pos):  # Exit
                    run = False
                elif DFS_Button.is_over(m_pos):  # Start DFS Algo
                    for row in board:
                        for cell in row:
                            cell.update_neighbor(board)
                    if start and end:
                        DFS(board,start,end)
                elif Clear_Button.is_over(m_pos):  # Clear
                    clear(board)
                elif Random_Button.is_over(m_pos):
                    board = make_board(ROWS,WIDTH)
                    start = None
                    end = None
                    board = random_obs(board)
                elif Dijkstra_button.is_over(m_pos):
                    for row in board:
                        for cell in row:
                            cell.update_neighbor(board)
                    Dijkstra(board,start,end)
                else:
                    row,col = get_clicked_pos(m_pos,ROWS,WIDTH)
                    cell = board[row][col]
                    if not start and cell != end:
                        start = cell
                        cell.make_start()
                    if not end and cell != start:
                        end = cell
                        cell.make_end()
                    elif cell != end and cell != start:
                        board[row][col].make_barrier()

            if pygame.mouse.get_pressed()[2]:
                m_pos = pygame.mouse.get_pos()
                row,col = get_clicked_pos(m_pos,ROWS,WIDTH)
                cell = board[row][col]
                cell.reset()
                cell.update_neighbor(board)
                if cell == start:
                    start = None
                if cell == end:
                    end = None
    pygame.quit()
# END MAIN


# Run program:
if __name__ == '__main__':
    main()





        


