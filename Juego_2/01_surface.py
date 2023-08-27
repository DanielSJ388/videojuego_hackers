import pygame
import sys

pygame.init()

whidth = 400
heigth = 500

surface = pygame.display.set_mode((whidth, heigth)) #Crear ventana

pygame.display.set_caption("Hola Mundo") #Poner titulo a la ventana

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #Clic en cerrar
            pygame.quit() #Cerrar pygame
            sys.exit() # Terminar la ejecucion del programa