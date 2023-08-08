import pygame
import sys

pygame.init()

whidth = 400
heigth = 500

surface = pygame.display.set_mode((whidth, heigth)) #Crear ventana

pygame.display.set_caption("Colores") #Poner titulo a la ventana

#RGB
# Crear colores / Clase Color
red = pygame.Color(255, 0, 0) # 0 - 255
green = pygame.Color(0, 255, 0)
blue = pygame.Color(0, 0, 255)

white = pygame.Color(255, 255, 255)
black = pygame.Color(0, 0, 0)

# Crear colores / Tuplas
my_color = (12, 249, 238)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #Clic en cerrar
            pygame.quit() #Cerrar pygame
            sys.exit() # Terminar la ejecucion del programa

    surface.fill(my_color) # Pintar la pantalla
    pygame.display.update() # Actualizar pantalla
