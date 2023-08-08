import pygame

# Inicializar Pygame
pygame.init()

# Definir dimensiones de la ventana
ventana_ancho = 800
ventana_alto = 600

tamanio_sprite = [100, 100]

# Crear la ventana
ventana = pygame.display.set_mode((ventana_ancho, ventana_alto))
pygame.display.set_caption("Ejemplo de Sprite en Pygame")

# Definir colores (opcional)
color_fondo = (0, 0, 0)  # Blanco

# Cargar las imágenes del sprite en una lista
sprites = [pygame.image.load(f'Recursos/Imagenes/Goku_Sprites/Goku{i}.png') for i in range(1, 5)]
sprites = [pygame.transform.scale(sprite, tamanio_sprite) for sprite in sprites]
# Inicializar el índice de imagen actual
indice_imagen_actual = 0

# Obtener el rectángulo del sprite (para manipular posición, tamaño, etc.)
sprite_rect = sprites[indice_imagen_actual].get_rect()

# Posición inicial del sprite en la ventana
sprite_x = ventana_ancho // 2 - sprite_rect.width // 2
sprite_y = ventana_alto // 2 - sprite_rect.height // 2

# Bucle principal del juego
ejecutando = True
while ejecutando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ejecutando = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                # Cambiar al siguiente índice de imagen del sprite
                indice_imagen_actual = (indice_imagen_actual + 1) % len(sprites)

    # Actualizar la lógica del juego aquí si es necesario

    # Borrar la ventana con el color de fondo
    ventana.fill(color_fondo)

    # Dibujar el sprite en la ventana en la posición actual
    ventana.blit(sprites[indice_imagen_actual], (sprite_x, sprite_y))

    # Actualizar la ventana
    pygame.display.flip()

# Salir del juego
pygame.quit()