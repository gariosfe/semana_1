def funcion_max_min(arr): #Creamos la funcion
    if not arr:
        return None, None
    
    numero_max  = max(arr) # utilizamos el minimo y el maximo que tiene python para ordenarlos
    numero_min = min(arr)  # mientras untilizamos el array

    return numero_max, numero_min

numeros_arr = [32, 1, 46, 5, 60, 70] # Se crea la lista
numero_max, numero_min = funcion_max_min(numeros_arr) # llamamos la funcion 
print(f"numero maximo = {numero_max}, numero minimo = {numero_min}") # se imprime la funcion 


