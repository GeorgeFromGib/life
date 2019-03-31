

from __future__ import print_function

from graphics import *
from life import Life

import time

life = Life(6, 6)
life.set_cell(1, True)
life.set_cell(2, True)
life.set_cell(3, True)


def show_grid():
    grid = life.get_grid()
    gx, gy = life.get_grid_dim()
    for i in range(len(grid)):
        print(grid[i], end='')
        if i % gx == gx - 1:
            print("")


# iter = 0
# while True:
#     print("Iteration {} Population {}".format(iter, life.get_population()))
#     show_grid()
#     x = raw_input("Enter to continue")
#     life.process_life()
#     iter += 1

win = GraphWin(width = 400, height = 400) # create a window
#win.setCoords(0, 0, 10, 10) # set the coordinates of the window; bottom left is (0, 0) and top right is (10, 10)
cells=[]
cell_width=400/6
gx, gy = life.get_grid_dim()
col=0;
row=0;
for f in range(gx * gy):
    cx=col*cell_width
    cy=row*cell_width
    cells.append(Rectangle(Point(cx,cy),Point(cx+cell_width,cy+cell_width)))
    cells[f].setFill('black')
    cells[f].setOutline('white')
    cells[f].draw(win)
    col+=1
    if f % gx == gx - 1:
        row+=1
        col=0
#mySquare = Rectangle(Point(1, 1), Point(9, 9)) # create a rectangle from (1, 1) to (9, 9)
#mySquare.draw(win) # draw it to the window
#mySquare.setFill('red')

def display_cells():
    grid=life.get_grid()
    for i in range(len(grid)):
        cells[i].setFill('yellow' if grid[i]=="*" else 'black')

while True:
     #print("Iteration {} Population {}".format(iter, life.get_population()))
     display_cells()
     time.sleep(5)
     life.process_life()

win.getMouse() # pause before closing
win.close()