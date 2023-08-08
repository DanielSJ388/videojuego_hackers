import pygame

# Inicializar Pygame
pygame.init()

# Definir dimensiones de la ventana
ventana_ancho = 800
ventana_alto = 600

# Tamaño de cada sprite individual en la sprite sheet
ancho_sprite = 48
alto_sprite = 48

# Cargar la sprite sheet
spritesheet_imagen = pygame.image.load('Recursos/Imagenes/Goku_Sprites/Sprite1.jpg')

# Crear una lista para almacenar todos los sprites individuales
sprites = []

# Extraer los sprites individuales de la sprite sheet y almacenarlos en la lista
for columna in range(0, spritesheet_imagen.get_height(), alto_sprite):
    for fila in range(0, spritesheet_imagen.get_width(), ancho_sprite):
        if columna + ancho_sprite <= spritesheet_imagen.get_width() and fila + alto_sprite <= spritesheet_imagen.get_height():
            sprite = spritesheet_imagen.subsurface(pygame.Rect(columna, fila, ancho_sprite, alto_sprite))
            sprites.append(sprite)


# Obtener el rectángulo del sprite (para manipular posición, tamaño, etc.)
sprite_rect = sprites[0].get_rect()

# Posición inicial del sprite en la ventana
sprite_x = ventana_ancho // 2 - sprite_rect.width // 2
sprite_y = ventana_alto // 2 - sprite_rect.height // 2

# Crear la ventana
ventana = pygame.display.set_mode((ventana_ancho, ventana_alto))
pygame.display.set_caption("Ejemplo de Sprite en Pygame")

# Bucle principal del juego
ejecutando = True
indice_frame = 0
reloj = pygame.time.Clock()

while ejecutando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ejecutando = False

    # Actualizar la lógica del juego aquí si es necesario

    # Borrar la ventana con el color de fondo
    ventana.fill((238, 59, 59))  # Rellenamos con color

    # Dibujar el sprite actual en la ventana en la posición actual
    ventana.blit(sprites[indice_frame], (sprite_x, sprite_y))

    # Actualizar el índice del frame para animar el sprite
    indice_frame = (indice_frame + 1) % len(sprites)

    # Limitar la velocidad de fotogramas a (n) fotogramas por segundo
    reloj.tick(5)

    # Actualizar la ventana
    pygame.display.flip()

# Salir del juego
pygame.quit()
