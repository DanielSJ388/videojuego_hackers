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

#Rectangulos Clase Rect

rect = pygame.Rect(100, 150, 120, 60) # Crear rectangulos
rect.center = (whidth//2, heigth//2) # Centrar el rectangulo en la pantalla

print(rect.x)
print(rect.y)

#Rectangulos Tuplas

rect_2 = (100, 100, 80, 40)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #Clic en cerrar
            pygame.quit() #Cerrar pygame
            sys.exit() # Terminar la ejecucion del programa

    surface.fill(my_color) # Pintar la pantalla

    pygame.draw.rect(surface, red, rect) # Pintar el rectagulo en la pantalla
    pygame.draw.rect(surface, green, rect_2)

    pygame.display.update() # Actualizar pantalla

