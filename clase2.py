import random
import time


# Genera una lista de números aleatorios
def generar_lista(tamano):
    return [random.randint(1, 100) for _ in range(tamano)]

#Aqui se junto las dos funciones de "maximo" y "sumar"
def maximo_suma(lista):
    maximo = lista[0]
    suma = 0
    for num in lista:
        if num > maximo:
            maximo = num
        suma += num
    return maximo, suma

# Main
if __name__ == "__main__":
    tamano_lista = 1000
    lista = generar_lista(tamano_lista)
    maximo = maximo_suma(lista)
    suma = maximo_suma(lista)

#funcion para el timpo del codigo
    start_time = time.time()
    
    maximo, suma = maximo_suma(lista)

    end_time = time.time()
    elapsed_time = end_time - start_time

    print(f"Lista: {lista}")
    print(f"Máximo: {maximo}")
    print(f"Suma: {suma}")
    print(f"Tiempo de ejecución: {elapsed_time:.6f} segundos")


