
'''
Edward Abel Guobadia
11-26-2022
Conways Game of life
'''

import pygame
from time import sleep
from sys import exit
import logging
logging.basicConfig(level = logging.DEBUG)

def draw_empty_board(screen):
    for x in range(0, 600, 24):
            for y in range(0, 600, 24):
                rect = pygame.Rect(x, y, 24, 24)
                pygame.draw.rect(screen, (179, 200, 232), rect)
                pygame.display.update()
    for x in range(0, 600, 25):
        for y in range(0, 600, 25):
            rect = pygame.Rect(x, y, 25, 25)
            pygame.draw.rect(screen, (255, 255, 255), rect, 1)
            pygame.display.update()

def count_neighbors(matrix, pos):
    (i, j) = pos
    count = 0
    neighbors = [(i - 1, j - 1), (i - 1, j + 0), (i - 1, j + 1),
                 (i + 0, j - 1),                 (i + 0, j + 1),
                 (i + 1, j - 1), (i + 1, j + 0), (i + 1, j + 1)]
    for i, j in neighbors:
        if i >= 0 and j >= 0:
            try:
                count += matrix[i][j]
            except:
                pass
    
    return count

def main():
    grid = [[0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0]]

    pygame.init()
    while True:
        #   QUIT event handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        #   opens game window
        screen = pygame.display.set_mode((600, 600))
        pygame.display.set_caption("Conway's Game of Life")
        pygame.display.update()

        #   draws starting game position
        draw_empty_board(screen)

        for i in range(0, 5):
            for j in range(0, 5):
                if grid[i][j] == 1:
                    pygame.draw.circle(screen, (255, 0, 0), (i * 25, j * 25), 6)
                    pygame.display.update()
                else:
                    continue

        sleep(100)

if __name__ == "__main__":
    main()
