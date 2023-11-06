import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Posición inicial de los robots
robots = [{'x': 0, 'y': i, 'detectado': False} for i in range(1, 51)]

# Posición de la fuente de calor
calor_x = 5
calor_y = 2

# Velocidad de los robots
velocidad = 0.1

fig, ax = plt.subplots()


def actualizar(frame):
    ax.clear()
    global robots

    for i, robot in enumerate(robots):
        distancia = ((robot['x'] - calor_x)**2 +
                     (robot['y'] - calor_y)**2)**0.5

        if distancia < 1:
            robot['detectado'] = True

        if robot['detectado']:
            # Calcula la posición alrededor del fuego
            angulo = 2 * np.pi * i / len(robots)
            objetivo_x = calor_x + np.cos(angulo)
            objetivo_y = calor_y + np.sin(angulo)
            # Mueve el robot hacia el objetivo
            robot['x'] += (objetivo_x - robot['x']) * velocidad
            robot['y'] += (objetivo_y - robot['y']) * velocidad
            ax.scatter(robot['x'], robot['y'],
                       color='violet', label='Apagando fuego')
        elif any(r['detectado'] for r in robots):
            # Si cualquier otro robot ha detectado el fuego, este robot se dirige hacia él
            robot['x'] += (calor_x - robot['x']) * velocidad
            robot['y'] += (calor_y - robot['y']) * velocidad
            ax.scatter(robot['x'], robot['y'], color='orange',
                       label='Dirigiéndose al fuego')
        else:
            # Si no se ha detectado el fuego, el robot avanza
            robot['x'] += velocidad
            ax.scatter(robot['x'], robot['y'],
                       color='blue', label='Buscando fuego')

        ax.scatter(calor_x, calor_y, color='red', label='Fuego')
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 51)

        # Eliminar duplicados en la leyenda
        handles, labels = ax.get_legend_handles_labels()
        by_label = dict(zip(labels, handles))
        ax.legend(by_label.values(), by_label.keys())


ani = animation.FuncAnimation(fig, actualizar, frames=100, interval=100)
plt.show()
