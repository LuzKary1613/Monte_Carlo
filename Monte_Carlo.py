import matplotlib.pyplot as plt
import numpy as np

def monte_carlo_pi(num_puntos):
    # Generando puntos aleatorios
    x = np.random.uniform(0, 1, num_puntos)
    y = np.random.uniform(0, 1, num_puntos)

    # Calculo para la distancia
    distancia = np.sqrt(x**2 + y**2)

    # Verificación del punto (dentro del circulo)
    dentro_circulo = distancia <= 1

    # calcular el valor de pi 
    aprox_pi = 4 * np.sum(dentro_circulo) / num_puntos

    return x, y, dentro_circulo, aprox_pi

def plot_monte_carlo(num_puntos):
    x, y, dentro_circulo, aprox_pi = monte_carlo_pi(num_puntos)

    # GRÁFICA
    fig, ax = plt.subplots()
    
    ax.scatter(x[dentro_circulo], y[dentro_circulo], color='blue', label='Dentro del círculo')
    ax.scatter(x[~dentro_circulo], y[~dentro_circulo], color='red', label='Fuera del círculo')

    # CIRCULO
    circulo = plt.Circle((0, 0), 1, edgecolor='black', facecolor='none')
    ax.add_patch(circulo)

    # CONFIGURACIÓN
    ax.set_aspect('equal', adjustable='box')
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_title(f'Aproximación de Pi: {aprox_pi:.6f}')
    ax.set_xlabel('Eje X')
    ax.set_ylabel('Eje Y')
    ax.legend()
    plt.show()

num_puntos = int(input('Ingrese la cantidad de puntos a generar: '))

# GENERACIÓN Y MOSTRACIÓN DEL GRAFO
plot_monte_carlo(num_puntos)
