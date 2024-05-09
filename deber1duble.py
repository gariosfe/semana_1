def funcion_duble(arr):
    n = len(arr) 

    for i in range(n): 
        for j in range(n - i - 1): 
            if arr[j] > arr[j + 1]: # si el numero es mayor lo cambiamos de posicion 
                arr[j], arr[j + 1] = arr[j + 1], arr[j] 


numeros_arr = [32, 1, 46, 5, 60, 70]   # se crea le lista 
funcion_duble(numeros_arr) #se llama la funcion

print("El arreglo ordenado:", numeros_arr) #se imprime el resultado 
