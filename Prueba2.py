import pygame
import random
import sys

# Clase Jugador
class Jugador:
    def __init__(self, x, y, imagen_path, ancho, altura):
        self.x = x
        self.y = y
        self.velocidad = 5
        self.vida = 100
        self.imagen_original = pygame.image.load(imagen_path)
        self.imagen = pygame.transform.scale(self.imagen_original, (ancho, altura))
        self.rect = self.imagen.get_rect()
        self.rect.topleft = (x, y)  # Establecer la posición del rectángulo de colisión

    def actualizar_rect_colision(self):
        self.rect.topleft = (self.x, self.y)
        # Ajustar manualmente el tamaño del rectángulo de colisión
        self.rect.inflate_ip(0.1, 0.1)

    def mover_arriba(self):
        self.y -= self.velocidad

    def mover_abajo(self):
        self.y += self.velocidad

    def mover_izquierda(self):
        self.x -= self.velocidad

    def mover_derecha(self):
        self.x += self.velocidad

    def recibir_danio(self, danio):
        self.vida -= danio
        self.velocidad = max(1, 5 - self.vida // 10)

    def dibujar(self, pantalla):
        pantalla.blit(self.imagen, (self.x, self.y))


# Carga de imágenes y música
pygame.init()
ventana_ancho, ventana_alto = 800, 600
pantalla = pygame.display.set_mode((ventana_ancho, ventana_alto))
pygame.display.set_caption("Chase the Player")

fondo = pygame.image.load("Recursos/Imagenes/Fondo.jpg")
fondo = pygame.transform.scale(fondo, (800, 600))
jugador1_imagen_path = "Recursos/Imagenes/Jugador1.png"
jugador2_imagen_path = "Recursos/Imagenes/Jugador2.png"

# Creación de los jugadores
jugador2 = Jugador(700, 300, jugador2_imagen_path, 50, 50)
jugador1 = Jugador(100, 300, jugador1_imagen_path, 50, 50)


# Inicialización del sonido de fondo
pygame.mixer.init()
pygame.mixer.music.load("Recursos/Sonidos/Dragon Ball Z Música de Pelea. (320 kbps).mp3")
pygame.mixer.music.play(-1)  # Reproducir en bucle continuo
pygame.mixer.music.set_volume(1)  # Ajustar el volumen al 50%

sonido_colision = pygame.mixer.Sound("Recursos/Sonidos/Sonido de golpe de dragon ball z (320 kbps).mp3")
sonido_colision.set_volume(0.5)

sonido_muerte = pygame.mixer.Sound("Recursos/Sonidos/Grito de vegeta. Dragón ball. Saga de boo. (320 kbps).mp3")

reloj = pygame.time.Clock()


# Control de velocidad del jugador 2
jugador2_velocidad = 3

# Variables para el movimiento aleatorio del jugador 2
jugador2_direccion_x = 0
jugador2_direccion_y = 0
jugador2_contador_cambio_dir = random.randint(50, 200)  # Número de fotogramas antes de cambiar de dirección


# Bucle principal del juego
tiempo_colision = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Movimiento del jugador 1 (controlado por el usuario)
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_w]:
        jugador1.mover_arriba()
    if teclas[pygame.K_s]:
        jugador1.mover_abajo()
    if teclas[pygame.K_a]:
        jugador1.mover_izquierda()
    if teclas[pygame.K_d]:
        jugador1.mover_derecha()

    # Movimiento aleatorio del jugador 2
    jugador2_contador_cambio_dir -= 1
    if jugador2_contador_cambio_dir == 0:
        jugador2_direccion_x = random.randint(-1, 1)  # -1: izquierda, 0: sin movimiento en el eje X, 1: derecha
        jugador2_direccion_y = random.randint(-1, 1)  # -1: arriba, 0: sin movimiento en el eje Y, 1: abajo
        jugador2_contador_cambio_dir = random.randint(50, 60)

    jugador2.x += jugador2_velocidad * jugador2_direccion_x
    jugador2.y += jugador2_velocidad * jugador2_direccion_y



    # Restricción para que el jugador 1 Y 2 no salgan de la pantalla
    jugador2.x = max(jugador2.x, 0)
    jugador2.x = min(jugador2.x, ventana_ancho - jugador2.rect.width)
    jugador2.y = max(jugador2.y, 0)
    jugador2.y = min(jugador2.y, ventana_alto - jugador2.rect.height)

    jugador1.x = max(jugador1.x, 0)
    jugador1.x = min(jugador1.x, ventana_ancho - jugador1.rect.width)
    jugador1.y = max(jugador1.y, 0)
    jugador1.y = min(jugador1.y, ventana_alto - jugador1.rect.height)

    # Ajustar el tamaño del rectángulo de colisión del jugador 1
    jugador1.actualizar_rect_colision()

    # Ajustar el tamaño del rectángulo de colisión del jugador 2
    jugador2.actualizar_rect_colision()

    # Colisión entre los jugadores
    if jugador1.rect.colliderect(jugador2.rect) and tiempo_colision == 0:
        jugador2.recibir_danio(10)
        sonido_colision.play()
        tiempo_colision = 100  # Tiempo de retraso para evitar que se aplique daño repetidamente

    # Tiempo de retraso después de la colisión
    if tiempo_colision > 0:
        tiempo_colision -= 1

    # Dibujar el fondo en la pantalla
    pantalla.blit(fondo, (0, 0))

    # Dibujar a los jugadores en la pantalla
    jugador1.dibujar(pantalla)
    jugador2.dibujar(pantalla)

    # Mostrar la vida del jugador 2 encima de él
    fuente = pygame.font.SysFont(None, 24)
    vida_texto = fuente.render(f"Vida: {jugador2.vida}", True, (255, 255, 255))
    pantalla.blit(vida_texto, (jugador2.x, jugador2.y - 30))

    # Verificar si el jugador 2 ha perdido todas sus vidas
    if jugador2.vida <= 0:
        sonido_muerte.play()
        mensaje = fuente.render("¡Has ganado el juego!", True, (255, 255, 255))
        pantalla.blit(mensaje, (ventana_ancho // 2 - mensaje.get_width() // 2, ventana_alto // 2 - mensaje.get_height() // 2))
        pygame.display.update()
        pygame.time.delay(5000)  # Mostrar el mensaje durante 3 segundos antes de cerrar el juego
        pygame.quit()
        sys.exit()

    # Actualizar la pantalla
    pygame.display.update()
    reloj.tick(60)  # Controla la velocidad de actualización del juego
