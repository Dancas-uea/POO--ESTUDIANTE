# Importa el módulo threading que permite trabajar con hilos (concurrencia)
import threading
# Importa el módulo time para funciones relacionadas con el tiempo (como sleep)
import time

# Define una función que será ejecutada por cada hilo
# Recibe dos parámetros: identificador (número del hilo) y delay (tiempo de espera)
def tarea_hilo(identificador, delay):
    # Bucle que se ejecutará 5 veces para cada hilo
    for i in range(5):
        # Imprime un mensaje mostrando qué hilo está ejecutando qué tarea
        print(f'Hilo {identificador}: Realizando tarea {i}')
        # Pausa la ejecución del hilo actual por 'delay' segundos
        time.sleep(delay)

# Crea el primer hilo, asignándole la función tarea_hilo con argumentos (1, 1)
# El hilo 1 tendrá un delay de 1 segundo entre tareas
hilo1 = threading.Thread(target=tarea_hilo, args=(1, 1))
# Crea el segundo hilo con delay de 0.8 segundos
hilo2 = threading.Thread(target=tarea_hilo, args=(2, 0.8))
# Crea el tercer hilo con delay de 1.2 segundos
hilo3 = threading.Thread(target=tarea_hilo, args=(3, 1.2))

# Inicia la ejecución del hilo1 (comienza a ejecutar tarea_hilo en paralelo)
hilo1.start()
# Inicia la ejecución del hilo2
hilo2.start()
# Inicia la ejecución del hilo3
hilo3.start()

# El método join() hace que el programa principal espere a que hilo1 termine
hilo1.join()
# Espera a que hilo2 termine
hilo2.join()
# Espera a que hilo3 termine
hilo3.join()

# Este mensaje se imprimirá solo cuando todos los hilos hayan terminado
print('Programa principal: Todas las tareas han sido completadas.')


