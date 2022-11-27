
'''
Edward Abel Guobadia
11-26-2022
Conways Game of life
'''

from time import sleep
from random import randint
from sys import exit
import pygame

pygame.init()

#Initialise the screen
xmax = 600 #Width of screen in pixels
ymax = 600 #Height of screen in pixels
screen = pygame.display.set_mode((xmax, ymax), 0, 24) #New 24-bit screen

def draw_empty_board(screen):
    for x in range(0, 600, 24):
            for y in range(0, 600, 24):
                rect = pygame.Rect(x, y, 24, 24)
                pygame.draw.rect(screen, (255, 255, 255), rect) #179, 200, 232
                pygame.display.update()
    #for x in range(0, 600, 25):
        #for y in range(0, 600, 25):
            #rect = pygame.Rect(x, y, 25, 25)
            #pygame.draw.rect(screen, (255, 255, 255), rect, 1)
            #pygame.display.update()

def evolve_cell(alive, neighbours):
    return neighbours == 3 or (alive and neighbours == 2)

def count_neighbours(grid, position):
    x,y = position
    neighbour_cells = [(x - 1, y - 1), (x - 1, y + 0), (x - 1, y + 1),
                       (x + 0, y - 1),                 (x + 0, y + 1),
                       (x + 1, y - 1), (x + 1, y + 0), (x + 1, y + 1)]
    count = 0
    for x,y in neighbour_cells:
        if x >= 0 and y >= 0:
            try:
                count += grid[x][y]
            except:
                pass
    return count

def make_empty_grid(x, y):
    grid = []
    for r in range(x):
        row = []
        for c in range(y):
            row.append(0)
        grid.append(row)
    return grid

def make_random_grid(x, y):
        grid = []
        for r in range(x):
            row = []
            for c in range(y):
                row.append(randint(0,1))
            grid.append(row)
        return grid

def evolve(grid):
    x = len(grid)
    y = len(grid[0])
    new_grid = make_empty_grid(x, y)
    for r in range(x):
        for c in range(y):
            cell = grid[r][c]
            neighbours = count_neighbours(grid, (r, c))
            new_grid[r][c] = 1 if evolve_cell(cell, neighbours) else 0
    return new_grid


def draw_block(x, y, alive_color):
    block_size = 25
    x *= block_size
    y *= block_size
    rect = pygame.Rect(x, y, 25, 25)
    center_point = ((x + (block_size / 2)), (y + (block_size / 2)))
    pygame.draw.circle(screen, alive_color, center_point, block_size / 2, 0)
    pygame.draw.rect(screen, alive_color, rect)


def main():
    cell_number = 0
    alive_color = pygame.Color(255, 255, 255)
    xlen = int(xmax / 25)
    ylen = int(ymax / 25)
    #draw_empty_board(screen)
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                #   make cell alive
                pass
            
        world = make_random_grid(xlen, ylen)
        for i in range(200):
            for x in range(xlen):
                for y in range(ylen):
                    alive = world[x][y]
                    cell_number += 1
                    if alive:
                        cell_color = alive_color
                        draw_block(x, y, cell_color)
                    else:
                        cell_color = (0, 0, 0)#179, 200, 232
                        draw_block(x, y, cell_color)
            pygame.display.flip()
            world = evolve(world)
            cell_number = 0
            sleep(0.1)

if __name__ == '__main__':
    main()