#!/usr/bin/python
import pygame, os, sys
from pygame.locals import *

# ================================
# 1. Inicialización y Configuración
# ================================
pygame.init()
fpsClock = pygame.time.Clock()
mainSurface = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Bricks - Calidad de Software')
black = pygame.Color(0, 0, 0)

# ================================
# 2. Configuración de Elementos del Juego
# -------------------------------
# Configuración de la paleta (bat)
bat = pygame.image.load('bat.png')       # Cargar imagen de la paleta
playerY = 540                            # Posición fija en Y
batRect = bat.get_rect()                 # Rectángulo de colisión
mousex, mousey = (0, playerY)             

# Configuración de la pelota (ball)
ball = pygame.image.load('ball.png')       # Cargar imagen de la pelota
ballRect = ball.get_rect()                 # Rectángulo de colisión
ballStartY = 200                           # Posición inicial en Y
ballSpeed = 3                              # Velocidad base
ballServed = False                         # Estado: la pelota aún no se ha lanzado
bx, by = (24, ballStartY)                  # Posiciones iniciales (x, y)
sx, sy = (ballSpeed, ballSpeed)            # Velocidad en cada eje
ballRect.topleft = (bx, by)                # Posicionar la pelota

# ================================
# 3. Función para Crear Ladrillos
# -------------------------------
def createBricks(pathToImg, rows, cols):
    """
    Crea una lista de rectángulos que representan ladrillos.
    Utiliza ciclos 'for' anidados para posicionar filas y columnas de ladrillos.
    """
    brick = pygame.image.load(pathToImg)   # Cargar imagen del ladrillo
    bricks = []                            # Lista para almacenar los rectángulos de cada ladrillo
    for y in range(rows):                  # Ciclo for para las filas
        brickY = (y * 24) + 100            # Posición Y para la fila de ladrillos
        for x in range(cols):              # Ciclo for para las columnas
            brickX = (x * 31) + 245        # Posición X para cada ladrillo
            width = brick.get_width()      # Ancho del ladrillo
            height = brick.get_height()    # Alto del ladrillo
            rect = Rect(brickX, brickY, width, height)
            bricks.append(rect)            # Agregar el ladrillo a la lista
    return bricks

# Crear los ladrillos (por ejemplo: 5 filas y 10 columnas)
bricks = createBricks('brick.png', 5, 10)
brick = pygame.image.load('brick.png')   # Guardamos la imagen para dibujarla después

# ================================
# 4. Bucle Principal del Juego
# ================================
while True:
    mainSurface.fill(black)  # Limpiar pantalla cada frame

    # --- DIBUJAR ELEMENTOS ---
    # Dibujar todos los ladrillos utilizando un ciclo 'for'
    for b in bricks:
        mainSurface.blit(brick, b)
    # Dibujar la paleta y la pelota
    mainSurface.blit(ball, ballRect)
    mainSurface.blit(bat, batRect)

    # --- GESTIÓN DE EVENTOS (IF/ELSE y ciclos for) ---
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEMOTION:
            mousex, mousey = event.pos
            # Uso de if/else para evitar que la paleta se salga de la pantalla
            if mousex < 800 - 55:
                batRect.topleft = (mousex, playerY)
            else:
                batRect.topleft = (800 - 55, playerY)
        elif event.type == MOUSEBUTTONUP and not ballServed:
            ballServed = True  # Lanzar la pelota

    # --- LÓGICA PRINCIPAL DEL JUEGO ---
    # Movimiento de la pelota si ya fue lanzada
    if ballServed:
        bx += sx
        by += sy
        ballRect.topleft = (bx, by)

    # Uso de if/else para detectar colisiones con los bordes
    if by <= 0:
        by = 0
        sy *= -1
    elif by >= 600 - 8:
        ballServed = False  # Reiniciar la pelota si toca el fondo
        bx, by = (24, ballStartY)
        ballSpeed = 3
        sx, sy = (ballSpeed, ballSpeed)
        ballRect.topleft = (bx, by)

    if bx <= 0:
        bx = 0
        sx *= -1
    elif bx >= 800 - 8:
        bx = 800 - 8
        sx *= -1

    # Colisión de la pelota con la paleta
    if ballRect.colliderect(batRect):
        by = playerY - 8
        sy *= -1

    # --- DETECCIÓN DE COLISIONES CON LOS LADRILLOS ---
    brickHitIndex = ballRect.collidelist(bricks)
    if brickHitIndex >= 0:
        hitBrick = bricks[brickHitIndex]
        mx = bx + 4  # Punto central aproximado en X
        my = by + 4  # Punto central aproximado en Y

        # Determinar en qué eje se debe invertir la velocidad
        if mx > hitBrick.x + hitBrick.width or mx < hitBrick.x:
            sx *= -1  # Rebote lateral
        else:
            sy *= -1  # Rebote vertical
        
        del bricks[brickHitIndex]  # Remover ladrillo golpeado

    # Actualizar pantalla y limitar FPS
    pygame.display.update()
    fpsClock.tick(60)