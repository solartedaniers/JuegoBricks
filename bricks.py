import pygame
import os
import sys
from pygame.locals import *

# ==============================
# 1. Inicialización y Configuración
# ==============================
pygame.init()
fpsClock = pygame.time.Clock()
mainSurface = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Bricks - Calidad de Software')
black = pygame.Color(0, 0, 0)

# ==============================
# 2. Función para Crear Ladrillos
# ==============================
def createBricks(rows, cols):
    """
    Crea una lista de rectángulos que representan ladrillos.
    """
    bricks = []
    for y in range(rows):
        brickY = (y * 24) + 100
        for x in range(cols):
            brickX = (x * 31) + 245
            rect = Rect(brickX, brickY, 30, 10)  # Tamaño ficticio si no hay imagen
            bricks.append(rect)
    return bricks

# ==============================
# 3. Lógica Principal del Juego
# ==============================
def main_loop():
    bat = pygame.image.load('bat.png')
    playerY = 540
    batRect = bat.get_rect()
    mousex, mousey = (0, playerY)             

    ball = pygame.image.load('ball.png')
    ballRect = ball.get_rect()
    ballStartY = 200
    ballSpeed = 3
    ballServed = False
    bx, by = (24, ballStartY)
    sx, sy = (ballSpeed, ballSpeed)
    ballRect.topleft = (bx, by)

    bricks = createBricks(5, 10)
    brick = pygame.image.load('brick.png')

    while True:
        mainSurface.fill(black)

        for b in bricks:
            mainSurface.blit(brick, b)
        mainSurface.blit(ball, ballRect)
        mainSurface.blit(bat, batRect)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                mousex, mousey = event.pos
                if mousex < 800 - 55:
                    batRect.topleft = (mousex, playerY)
                else:
                    batRect.topleft = (800 - 55, playerY)
            elif event.type == MOUSEBUTTONUP and not ballServed:
                ballServed = True

        if ballServed:
            bx += sx
            by += sy
            ballRect.topleft = (bx, by)

        if by <= 0:
            sy *= -1
        elif by >= 600 - 8:
            ballServed = False
            bx, by = (24, ballStartY)
            ballSpeed = 3
            sx, sy = (ballSpeed, ballSpeed)
            ballRect.topleft = (bx, by)

        if bx <= 0 or bx >= 800 - 8:
            sx *= -1

        if ballRect.colliderect(batRect):
            sy *= -1

        pygame.display.update()
        fpsClock.tick(60)

# ==============================
# 4. Evitar que se ejecute con pytest
# ==============================
if __name__ == "__main__":
    main_loop()
