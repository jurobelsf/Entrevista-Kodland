#Cargamos librerías

import pygame
import random
import sys

pygame.init()

# Dimensiones de la ventana del juego:

ANCHO = 600
ALTO = 600
VENTANA = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("¡Lluvia de hamburguesas!")

# Colores para cada parte del juego:

BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)  # Lava
AZUL = (0, 0, 255)
AMARILLO = (255, 255, 0) # Brillo del Tesoro
ORO = (255, 215, 0)      
ROJO_OSCURO = (150, 0, 0) # Base de la Lava


# Colores para la Hamburguesa
CAFE = (139, 69, 19)
NARANJA = (255, 165, 0)
# Colores para el Policía (Jugador)
AZUL_MARINO = (0, 0, 128) 
GRIS_CLARO = (200, 200, 200)

# Colores de la pantalla:
AZUL_OSCURO_FONDO = (25, 25, 50) 
BORDE_COLOR = (100, 100, 150)    

###############
FPS = 60
reloj = pygame.time.Clock()

##########################3


# Uso de funciones propias:

def dibujar_texto(superficie, texto, tamano, x, y, color=BLANCO):
    fuente = pygame.font.SysFont("Arial", tamano)
    etiqueta = fuente.render(texto, True, color)
    rectangulo = etiqueta.get_rect(center=(x, y))
    superficie.blit(etiqueta, rectangulo)

def dibujar_borde():
    grosor = 5
    pygame.draw.rect(VENTANA, BORDE_COLOR, (0, 0, ANCHO, grosor))
    pygame.draw.rect(VENTANA, BORDE_COLOR, (0, ALTO - grosor, ANCHO, grosor))
    pygame.draw.rect(VENTANA, BORDE_COLOR, (0, 0, grosor, ALTO))
    pygame.draw.rect(VENTANA, BORDE_COLOR, (ANCHO - grosor, 0, grosor, ALTO))

def dibujar_jugador(x, y):
    pygame.draw.rect(VENTANA, AZUL_MARINO, (x, y, 40, 40))
    pygame.draw.rect(VENTANA, AZUL_MARINO, (x + 5, y - 10, 30, 10))
    pygame.draw.rect(VENTANA, NEGRO, (x + 10, y - 5, 20, 5))
    pygame.draw.circle(VENTANA, AMARILLO, (x + 20, y + 15), 3)

def dibujar_hamburguesa(x, y):
    pygame.draw.rect(VENTANA, NARANJA, (x, y, 40, 10))
    pygame.draw.rect(VENTANA, CAFE, (x, y + 10, 40, 15))
    pygame.draw.rect(VENTANA, NARANJA, (x, y + 25, 40, 10))

def dibujar_tesoro(x, y):
    center_x, center_y = x + 15, y + 15
    pygame.draw.circle(VENTANA, ORO, (center_x, center_y), 15)
    pygame.draw.circle(VENTANA, CAFE, (center_x, center_y), 15, 2)
    pygame.draw.circle(VENTANA, AMARILLO, (center_x, center_y), 8)

def dibujar_lava(x, y):
    pygame.draw.rect(VENTANA, ROJO_OSCURO, (x, y, 50, 50))
    pygame.draw.rect(VENTANA, ROJO, (x + 5, y + 5, 40, 40))
    pygame.draw.circle(VENTANA, NARANJA, (x + 10, y + 40), 5)
    pygame.draw.circle(VENTANA, AMARILLO, (x + 40, y + 10), 4)
    pygame.draw.circle(VENTANA, NARANJA, (x + 25, y + 25), 6)


###########------------------------------------
# Juego 1:

def crear_enemigo():
    return [random.randint(0, ANCHO - 40), -50, 40, 40, random.randint(3, 7)]

def juego_esquivar():
    px = ANCHO // 2
    py = ALTO - 80
    velocidad = 7
    enemigos = [crear_enemigo() for _ in range(5)]
    puntos = 0
    jugando = True
    while jugando:
        reloj.tick(FPS)
        VENTANA.fill(AZUL_OSCURO_FONDO) 
        dibujar_borde()

        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT] and px > 0:
            px -= velocidad
        if teclas[pygame.K_RIGHT] and px < ANCHO - 40:
            px += velocidad

        for e in enemigos:
            e[1] += e[4]
            dibujar_hamburguesa(e[0], e[1])

            if e[1] > ALTO:
                e[:] = crear_enemigo()
                puntos += 10

            r_jugador = pygame.Rect(px, py, 40, 40)
            r_enemigo = pygame.Rect(e[0], e[1], 40, 40)

            if r_jugador.colliderect(r_enemigo):
                pantalla_fin(puntos, "No00oO, te cayó una hamburguesa :c")
                return

        dibujar_jugador(px, py)
        dibujar_texto(VENTANA, f"Puntos: {puntos}", 30, 80, 30)

        pygame.display.update()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit(); sys.exit()

# Juego 2:

def juego_atrapar():
    px = ANCHO // 2
    py = ALTO // 2
    velocidad = 7

    moneda_x = random.randint(50, ANCHO - 50)
    moneda_y = random.randint(50, ALTO - 50)

    obstaculos = []
    for _ in range(3):
        ox = random.randint(0, ANCHO - 50)
        oy = random.randint(0, ALTO - 50)
        if abs(ox - ANCHO//2) < 100 and abs(oy - ALTO//2) < 100:
            ox = 100
        obstaculos.append(pygame.Rect(ox, oy, 50, 50))

    puntos = 0
    tiempo_total = 15
    tiempo_inicio = pygame.time.get_ticks()

    jugando = True
    while jugando:
        reloj.tick(FPS)
        VENTANA.fill(AZUL_OSCURO_FONDO) 
        dibujar_borde() 

        tiempo_restante = tiempo_total - (pygame.time.get_ticks() - tiempo_inicio) / 1000
        if tiempo_restante <= 0:
            pantalla_fin(puntos, "Se acabó el tiempito :c")
            return

        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT] and px > 0: px -= velocidad
        if teclas[pygame.K_RIGHT] and px < ANCHO - 40: px += velocidad
        if teclas[pygame.K_UP] and py > 0: py -= velocidad
        if teclas[pygame.K_DOWN] and py < ALTO - 40: py += velocidad

        r_jugador = pygame.Rect(px, py, 40, 40)
        r_moneda = pygame.Rect(moneda_x, moneda_y, 30, 30)

        if r_jugador.colliderect(r_moneda):
            puntos += 1
            moneda_x = random.randint(50, ANCHO - 50)
            moneda_y = random.randint(50, ALTO - 50)

        for obs in obstaculos:
            if r_jugador.colliderect(obs):
                pantalla_fin(puntos, "Te quemaste!!!, chocaste con la lava :c")
                return

        dibujar_tesoro(moneda_x, moneda_y)
        for obs in obstaculos:
            dibujar_lava(obs.x, obs.y)

        dibujar_jugador(px, py)
        dibujar_texto(VENTANA, f"Puntos: {puntos}", 30, 80, 30)
        dibujar_texto(VENTANA, f"Tiempo: {int(tiempo_restante)}", 30, ANCHO - 80, 30)

        pygame.display.update()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit(); sys.exit()

################################################
# Pantalla final juego

def pantalla_fin(puntaje, mensaje):
    esperando = True
    while esperando:
        VENTANA.fill(AZUL_OSCURO_FONDO) # Fondo actualizado
        dibujar_borde() # Dibujar borde
        
        # Tamaño de fuente reducido a 40
        dibujar_texto(VENTANA, mensaje, 40, ANCHO//2, 200, ROJO) 
        dibujar_texto(VENTANA, f"Puntaje Final: {puntaje}", 40, ANCHO//2, 300)
        dibujar_texto(VENTANA, "Presiona ENTER para volver al menú", 25, ANCHO//2, 400)

        pygame.display.update()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RETURN:
                    esperando = False

###################---------------------------
# Menú

def menu_principal():
    ejecutando = True
    while ejecutando:
        VENTANA.fill(AZUL_OSCURO_FONDO)
        dibujar_borde() 
        
        dibujar_texto(VENTANA, "¡Lluvia de hamburguesas!", 50, ANCHO//2, 50, AZUL)


        
        # Línea 1
        dibujar_texto(VENTANA, "Eres el policía de lluvia de hamburguesas :3", 22, ANCHO//2, 120, GRIS_CLARO)

        # Línea 2
        dibujar_texto(VENTANA, "JUEGO 1:", 20, 80, 160, GRIS_CLARO)
        dibujar_texto(VENTANA, "Tendrás que esquivar las hamburguesas que caen del cielo.", 20, ANCHO//2 + 50, 190, BLANCO)

        # Línea 3-4
        dibujar_texto(VENTANA, "JUEGO 2:", 20, 80, 240, GRIS_CLARO)
        dibujar_texto(VENTANA, "Busca un tesoro de oro :D, pero, ¡ten cuidado!", 20, ANCHO//2 + 50, 270, BLANCO)
        dibujar_texto(VENTANA, "¡Hay lava en el camino y te puedes quemar! >:c", 20, ANCHO//2 + 50, 300, BLANCO)
        
        # Opciones del menu
        dibujar_texto(VENTANA, "1. Esquiva Hamburguesas", 30, ANCHO//2, 380)
        dibujar_texto(VENTANA, "2. Atrapa el Tesoro (Con Trampas)", 30, ANCHO//2, 440)
        dibujar_texto(VENTANA, "3. Salir", 30, ANCHO//2, 510)

        dibujar_texto(VENTANA, "Presiona el número de tu opción", 20, ANCHO//2, 570)

        pygame.display.update()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit(); sys.exit()

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_1:
                    juego_esquivar()
                elif evento.key == pygame.K_2:
                    juego_atrapar()
                elif evento.key == pygame.K_3:
                    pygame.quit(); sys.exit()

menu_principal()