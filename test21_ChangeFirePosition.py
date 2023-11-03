import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
import random

# Número de robots
num_robots = 5

# Posición inicial de los robots
robots = [{'x': 5, 'y': 5, 'detectado': False, 'angulo': 2 * np.pi *
           random.random(), 'distancia': 0, 'regresando': False} for _ in range(num_robots)]

# Posición de la fuente de calor
calor_x = 8
calor_y = 8

# Velocidad de los robots
velocidad = 0.5

fig, ax = plt.subplots()


def cambiar_posicion_fuego():
    global calor_x, calor_y
    calor_x = float(input("Ingrese la coordenada x del fuego: "))
    calor_y = float(input("Ingrese la coordenada y del fuego: "))


def mover_hacia_fuego(robot):
    robot['x'] += (calor_x - robot['x']) * velocidad
    robot['y'] += (calor_y - robot['y']) * velocidad
    ax.scatter(robot['x'], robot['y'], color='violet', label='Apagando fuego')


def mover_aleatoriamente(robot):
    if robot['regresando']:
        robot['x'] -= np.cos(robot['angulo']) * velocidad
        robot['y'] -= np.sin(robot['angulo']) * velocidad
    else:
        robot['x'] += np.cos(robot['angulo']) * velocidad
        robot['y'] += np.sin(robot['angulo']) * velocidad
        robot['distancia'] += velocidad
    ax.scatter(robot['x'], robot['y'], color='blue', label='Buscando fuego')


def actualizar(frame):
    ax.clear()
    global robots

    for i, robot in enumerate(robots):
        distancia = ((robot['x'] - calor_x)**2 +
                     (robot['y'] - calor_y)**2)**0.5

        if distancia < 1:
            robot['detectado'] = True

        if robot['detectado']:
            mover_hacia_fuego(robot)
        elif any(r['detectado'] for r in robots):
            mover_hacia_fuego(robot)
        else:
            if robot['distancia'] < 2 * ((calor_x - 5)**2 + (calor_y - 5)**2)**0.5 and not robot['regresando']:
                mover_aleatoriamente(robot)
            else:
                robot['regresando'] = True
                mover_aleatoriamente(robot)
                if robot['x'] == 5 and robot['y'] == 5:
                    robot['angulo'] = 2 * np.pi * random.random()
                    robot['distancia'] = 0
                    robot['regresando'] = False

        ax.scatter(calor_x, calor_y, color='red', label='Fuego')
        ax.set_xlim(0, 20)
        ax.set_ylim(0, 21)

        handles, labels = ax.get_legend_handles_labels()
        by_label = dict(zip(labels, handles))
        ax.legend(by_label.values(), by_label.keys())


cambiar_posicion_fuego()
ani = animation.FuncAnimation(fig, actualizar, frames=100, interval=100)
plt.show()
