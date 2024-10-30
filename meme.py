import pygame

# Entrada de datos
peso = int(input("Ingresa tu peso: "))

# Inicializar pygame
pygame.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("meme")

# Cargar y escalar imagen
imagen = pygame.image.load("otros/meme.jpg")  # Verifica que la imagen exista y la extensión sea correcta
imagen = pygame.transform.scale(imagen, (400, 400))
rect = imagen.get_rect(center=(300, 200))

# Variables para la rotación
angulo = 0
reloj = pygame.time.Clock()

# Cargar y reproducir música
pygame.mixer.music.load("otros/oye-gela-escuchate-esto-saturado.mp3")  # Verifica que el archivo de música exista
pygame.mixer.music.play(-1)  # Reproduce en bucle

# Bucle del juego
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()  # Corrige la llamada a pygame.quit()
            quit()  # Salir del programa
    
    # Rotación de la imagen
    angulo += 3
    imagen_rotando = pygame.transform.rotate(imagen, angulo)
    rect_rotando = imagen_rotando.get_rect(center=rect.center)

    # Dibujar en la pantalla
    screen.fill((255, 255, 255))  # Usa una tupla para el color (R, G, B)
    screen.blit(imagen_rotando, rect_rotando.topleft)

    # Actualizar pantalla
    pygame.display.flip()
    reloj.tick(60)
