import pygame
import sys

pygame.init()

whidth = 400
heigth = 500

surface = pygame.display.set_mode((whidth, heigth))  # Crear ventana

pygame.display.set_caption("Colores")  # Poner titulo a la ventana

# RGB
# Crear colores / Clase Color
red = pygame.Color(255, 0, 0)  # 0 - 255
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

white = pygame.Color(255, 255, 255)
black = pygame.Color(0, 0, 0)


surface2 = pygame.Surface((200, 200))
surface2.fill(green)

rect = surface2.get_rect()

rect.center = (whidth / 2, heigth / 2)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # Clic en cerrar
            pygame.quit()  # Cerrar pygame
            sys.exit()  # Terminar la ejecucion del programa

    surface.fill(white)  # Pintar la pantalla

    surface.blit(surface2, rect)# Pintar la pantalla 2 sobre pantalla 1

    pygame.draw.rect(surface2, red, (100, 50, 80, 40))

    pygame.display.update()  # Actualizar pantalla

