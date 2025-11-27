# Proyecto: Lluvia de Hamburguesas

Este proyecto cuenta con dos juegos desarrollados en Python utilizando
la librería **Pygame**. Fue diseñado como un proyecto práctico en el marco
de la entrevista de trabajo de Kodland. En este, se evidencian el uso de:

-   La librería Pygame\
-   Funciones personalizadas\
-   Menús y pantallas finales\
-   Temporizadores y enemigos aleatorios

El jugador tomará el papel del policía de la película Lluvia de Hamburguesas. 

------------------------------------------------------------------------

## Contenido del Proyecto

### **Menú Principal**

El jugador puede elegir: 1. Esquiva Hamburguesas\
2. Atrapa el Tesoro (con obstáculos)\
3. Salir del juego

------------------------------------------------------------------------

## JUEGO 1: Esquiva las Hamburguesas

### **Objetivo**

Mover al jugador de izquierda a derecha para evitar la lluvia de hamburguesas

### **Mecánicas**

-   Hamburguesas caen desde posiciones aleatorias.\
-   Cada vez que una sale de la pantalla, el jugador gana **10
    puntos**.\
-   Si una hamburguesa toca al jugador, pierde.

### **Controles**

Flechas izquierda y derecha.

------------------------------------------------------------------------

## 🎮 JUEGO 2: Atrapa el Tesoro

### **Objetivo**

Atrapar monedas evitando zonas de lava.

### **Mecánicas**

-   Cada moneda vale **1 punto**.\
-   Tocar lava hace perder.\
-   Temporizador de **15 segundos**.\
-   Si el tiempo llega a cero, termina el juego.

### **Controles**

Flechas direccionales.

------------------------------------------------------------------------

## Funciones Personalizadas

-   `dibujar_texto()`\
-   `dibujar_borde()`\
-   `dibujar_jugador()`\
-   `dibujar_hamburguesa()`\
-   `dibujar_tesoro()`\
-   `dibujar_lava()`\
-   `crear_enemigo()`\
-   `pantalla_fin()`

------------------------------------------------------------------------
