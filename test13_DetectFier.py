import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Número de robots
num_robots = 10

# Posición inicial de los robots
robots = [{'x': 5, 'y': 5, 'detectado': False, 'angulo': 2 *
           np.pi * i / num_robots} for i in range(num_robots)]

# Posición de la fuente de calor
calor_x = 8
calor_y = 8

# Velocidad de los robots
velocidad = 0.1

fig, ax = plt.subplots()


def actualizar(frame):
    ax.clear()
    global robots

    for i, robot in enumerate(robots):
        distancia = ((robot['x'] - calor_x)**2 +
                     (robot['y'] - calor_y)**2)**0.5

        # Aumentamos la distancia de detección a 1
        if distancia < 1 and not any(r['detectado'] for r in robots):
            robot['detectado'] = True

        if robot['detectado']:
            # Mueve el robot hacia el fuego
            robot['x'] += (calor_x - robot['x']) * velocidad
            robot['y'] += (calor_y - robot['y']) * velocidad
            ax.scatter(robot['x'], robot['y'],
                       color='violet', label='Apagando fuego')
        elif any(r['detectado'] for r in robots):
            # Si cualquier otro robot ha detectado el fuego, este robot se dirige hacia él
            robot['x'] += (calor_x - robot['x']) * velocidad
            robot['y'] += (calor_y - robot['y']) * velocidad
            ax.scatter(robot['x'], robot['y'], color='orange',
                       label='Dirigiéndose al fuego')
        else:
            # Si no se ha detectado el fuego, el robot avanza en línea recta hacia su punto objetivo en la circunferencia del círculo.
            angulo = 2 * np.pi * i / len(robots)
            # Ajustamos el punto objetivo para mostrar mejor el movimiento radial inicial
            objetivo_x = 5 + np.cos(robot['angulo']) * frame / 10
            # Ajustamos el punto objetivo para mostrar mejor el movimiento radial inicial
            objetivo_y = 5 + np.sin(robot['angulo']) * frame / 10
            robot['x'] += (objetivo_x - robot['x']) * velocidad
            robot['y'] += (objetivo_y - robot['y']) * velocidad
            ax.scatter(robot['x'], robot['y'],
                       color='blue', label='Buscando fuego')

        ax.scatter(calor_x, calor_y, color='red', label='Fuego')
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 11)

        # Eliminar duplicados en la leyenda
        handles, labels = ax.get_legend_handles_labels()
        by_label = dict(zip(labels, handles))
        ax.legend(by_label.values(), by_label.keys())


ani = animation.FuncAnimation(fig, actualizar, frames=100, interval=100)
plt.show()
