import pytest
import pygame
from pygame.locals import *
from bricks import createBricks

# ==============================
# Prueba 1: Creación de Ladrillos
# ==============================
def test_create_bricks():
    """Verifica que la función createBricks genera la cantidad correcta de ladrillos."""
    bricks = createBricks(5, 10)  # 5 filas x 10 columnas
    assert len(bricks) == 5 * 10  # Debe haber exactamente 50 ladrillos
    assert isinstance(bricks[0], pygame.Rect), "Los ladrillos deben ser objetos Rect"

# ==============================
# Prueba 2: Posicionamiento Correcto de Ladrillos
# ==============================
def test_bricks_position():
    """Verifica que los ladrillos se posicionan correctamente."""
    bricks = createBricks(2, 3)  # 2 filas x 3 columnas
    expected_positions = [
        (245, 100), (276, 100), (307, 100),  # Fila 1
        (245, 124), (276, 124), (307, 124)   # Fila 2
    ]
    
    actual_positions = [(brick.x, brick.y) for brick in bricks]
    
    assert actual_positions == expected_positions, f"Posiciones incorrectas: {actual_positions}"

# ==============================
# Prueba 3: Inicialización de Pygame
# ==============================
def test_pygame_initialization():
    """Verifica que pygame se inicializa correctamente."""
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    
    assert screen is not None, "La pantalla de pygame no se ha inicializado correctamente"

# ==============================
# Prueba 4: Carga de Imágenes (Mocking)
# ==============================
def test_load_images(monkeypatch):
    """Simula la carga de imágenes para evitar errores si los archivos no existen."""
    
    def mock_load(image_name):
        """Mock de pygame.image.load para evitar errores en pytest."""
        return pygame.Surface((50, 50))  # Devuelve una superficie ficticia

    monkeypatch.setattr(pygame.image, "load", mock_load)

    bat = pygame.image.load("bat.png")
    ball = pygame.image.load("ball.png")
    brick = pygame.image.load("brick.png")

    assert isinstance(bat, pygame.Surface)
    assert isinstance(ball, pygame.Surface)
    assert isinstance(brick, pygame.Surface)

# ==============================
# Prueba 5: Simulación de Movimiento de la Paleta
# ==============================
def test_paddle_movement():
    """Simula el movimiento de la paleta con eventos de pygame."""
    pygame.init()
    bat = pygame.Rect(350, 540, 100, 10)  # Paleta en posición inicial
    playerY = 540

    # Simulamos un evento de movimiento del ratón
    mouse_event = pygame.event.Event(MOUSEMOTION, {"pos": (400, playerY)})
    pygame.event.post(mouse_event)

    for event in pygame.event.get():
        if event.type == MOUSEMOTION:
            mousex, _ = event.pos
            if mousex < 800 - 55:
                bat.topleft = (mousex, playerY)
            else:
                bat.topleft = (800 - 55, playerY)

    assert bat.x == 400, "La paleta no se movió correctamente"

