def funcion_max_min(arr):
    if not arr:
        return None, None
    
    numero_max  = max(arr)
    numero_min = min(arr)

    return numero_max, numero_min

numeros_arr = [32, 1, 46, 5, 60, 70]
numero_max, numero_min = funcion_max_min(numeros_arr)
print(f"numero maximo = {numero_max}, numero minimo = {numero_min}")


