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

# Directorio base del script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGES_DIR = os.path.join(BASE_DIR, "images")  # Ruta correcta de imágenes

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
    # Cargar imágenes con rutas dinámicas
    bat = pygame.image.load(os.path.join(IMAGES_DIR, "bat.png"))
    playerY = 540
    batRect = bat.get_rect()
    mousex, mousey = (0, playerY)             

    ball = pygame.image.load(os.path.join(IMAGES_DIR, "ball.png"))
    ballRect = ball.get_rect()
    ballStartY = 200
    ballSpeed = 3
    ballServed = False
    bx, by = (24, ballStartY)
    sx, sy = (ballSpeed, ballSpeed)
    ballRect.topleft = (bx, by)

    bricks = createBricks(5, 10)
    brick = pygame.image.load(os.path.join(IMAGES_DIR, "brick.png"))

    while True:
        mainSurface.fill(black)

        # Dibujar ladrillos y verificar colisión con la bola
        bricks_to_remove = []
        for b in bricks:
            mainSurface.blit(brick, b)
            if ballRect.colliderect(b):  # Detectar colisión con la bola
                bricks_to_remove.append(b)  # Marcar ladrillo para eliminar
                sy *= -1  # Invertir dirección vertical de la bola
        
        # Eliminar los ladrillos que han sido impactados
        for b in bricks_to_remove:
            bricks.remove(b)

        # Dibujar la bola y la paleta
        mainSurface.blit(ball, ballRect)
        mainSurface.blit(bat, batRect)

        # Manejo de eventos
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

        # Movimiento de la bola
        if ballServed:
            bx += sx
            by += sy
            ballRect.topleft = (bx, by)

        # Colisiones con los bordes
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

        # Colisión con la paleta
        if ballRect.colliderect(batRect):
            sy *= -1

        pygame.display.update()
        fpsClock.tick(60)

# ==============================
# 4. Evitar que se ejecute con pytest
# ==============================
if __name__ == "__main__":
    main_loop()
