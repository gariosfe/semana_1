def funcion_sort(arr, size):
    for d in range(size):
        min_indi = d  
    
        for i in range(d + 1, size):
            if arr[i] < arr[min_indi]:
                min_indi = i  

        arr[d], arr[min_indi] = arr[min_indi], arr[d]  

numeros_arr = [-32, 1, -46, 5, 60, -70, 12]  

size = len(numeros_arr)  

funcion_sort(numeros_arr, size)  

print("El arreglo ordenado:", numeros_arr) 
