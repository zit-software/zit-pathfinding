# A*
from queue import PriorityQueue
from GUI import draw
from constant.sound import *
from constant.image import *
from common import *

def AStar(board, start, end):
    count = 0
    previous = start
    open_set = PriorityQueue()
    open_set.put((0, count, start)) # Adding the starting node to the open_set (f_score, count, node)
    came_from = {} # To store the interior that the current node came from.
    g_score = {cell: float("inf") for row in board for cell in row}  # set every node's g_score to inf
    g_score[start] = 0
    f_score = {cell : float("inf") for row in board for cell in row}  # set every node's f_score to inf
    f_score[start] = h(start.get_pos(),end.get_pos())
    open_set_hash= {start}# To indicate whether a node is in the queue or not.
    while not open_set.empty():
        pygame.mixer.Sound.play(swimmingSound)
        pygame.time.wait(200)
        current = open_set.get()[2]
        if previous == start:
            previous.setImage(startImg)
            current.setImage(duckImg)
        else:
            previous.setImage(footPrintImg)
            current.setImage(duckImg)
        previous = current

        open_set_hash.remove(current)

        if current == end:
            current.setImage(finishLineImg)
            reconstruct_path(came_from,start,end,board)
            return True

        for neighbor in current.neighbour:
            temp_g_score = g_score[current] + 1
            if temp_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = temp_g_score
                f_score[neighbor] = g_score[neighbor] + h((neighbor.get_pos()),end.get_pos())
                if neighbor not in open_set_hash:
                    count += 1
                    open_set.put((f_score[neighbor],count,neighbor))
                    open_set_hash.add(neighbor)
                    if neighbor != end:  # Avoid covering the end cell
                        neighbor.make_open()
        draw(WIN, board, ROWS, WIDTH)
        if current != start:  # Avoid covering the start cell
            current.make_closed()


    return False


def h(p1, p2):
    r1,c1 = p1
    r2,c2 = p2
    return abs(r1-r2) + abs(c1 - c2)

# END A*