# BEEBot Bombero

### 1. Requerimientos:

```
pip install matplotlib
pip install numpy
```

### 2. Algoritmo de funcionamiento

- Definir el número de robots y sus propiedades iniciales (posición, ángulo, distancia, si están regresando).
- Definir la posición de la fuente de calor.
- Definir la velocidad de los robots.
- Definir una función para mover un robot hacia la fuente de calor.
- Definir una función para mover un robot aleatoriamente.
- Definir una función para actualizar la posición de los robots en cada frame de la animación:
- Para cada robot, calcular la distancia a la fuente de calor.
  - Si la distancia es menor que X, marcar el robot como 'detectado'.
  - Si el robot ha 'detectado' la fuente de calor, moverlo hacia la fuente de calor.
  - Si cualquier robot ha 'detectado' la fuente de calor, mover todos los robots hacia la fuente de calor.
  - Si no, mover el robot aleatoriamente.
  - Si el robot ha alcanzado una cierta distancia y no está 'regresando', marcarlo como 'regresando' y moverlo aleatoriamente de vuelta al punto de inicio.
  - Si el robot ha regresado al punto de inicio, reiniciar su ángulo y distancia y marcarlo como no 'regresando'
  - Dibujar la posición de la fuente de calor y los robots en el eje
  - Actualizar la leyenda

#### 3. Versión vigente:

La versión vigente del proyecto es [Test #19](https://github.com/odaliz-r2/beeBot_bombero/blob/main/test19_MoreReal.py)
