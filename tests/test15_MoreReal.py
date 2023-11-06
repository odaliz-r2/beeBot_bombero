import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import random

# Número de robots
num_robots = 10

# Posición inicial de los robots
robots = [{'x': 5, 'y': 5, 'detectado': False, 'angulo': 2 *
           np.pi * random.random()} for _ in range(num_robots)]

# Posición de la fuente de calor
calor_x = 8
calor_y = 8

# Velocidad de los robots
velocidad = 0.1

fig, ax = plt.subplots()


def mover_hacia_fuego(robot):
    robot['x'] += (calor_x - robot['x']) * velocidad
    robot['y'] += (calor_y - robot['y']) * velocidad
    ax.scatter(robot['x'], robot['y'], color='violet', label='Apagando fuego')


def mover_aleatoriamente(robot):
    robot['x'] += np.cos(robot['angulo']) * velocidad
    robot['y'] += np.sin(robot['angulo']) * velocidad
    ax.scatter(robot['x'], robot['y'], color='blue', label='Buscando fuego')


def actualizar(frame):
    ax.clear()
    global robots

    for robot in robots:
        distancia = ((robot['x'] - calor_x)**2 +
                     (robot['y'] - calor_y)**2)**0.5

        if distancia < 1 and not any(r['detectado'] for r in robots):
            robot['detectado'] = True

        if robot['detectado']:
            mover_hacia_fuego(robot)
        elif any(r['detectado'] for r in robots):
            mover_hacia_fuego(robot)
        else:
            mover_aleatoriamente(robot)

        ax.scatter(calor_x, calor_y, color='red', label='Fuego')
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 11)

        handles, labels = ax.get_legend_handles_labels()
        by_label = dict(zip(labels, handles))
        ax.legend(by_label.values(), by_label.keys())


ani = animation.FuncAnimation(fig, actualizar, frames=100, interval=100)
plt.show()
