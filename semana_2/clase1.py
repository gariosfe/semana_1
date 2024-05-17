def funcion_sort(arr, size):
    for d in range(size):
        min_indi = d  
    
        for i in range(d + 1, size):
            if arr[i] < arr[min_indi]:
                min_indi = i  

        arr[d], arr[min_indi] = arr[min_indi], arr[d]  


def funcion_ordenamiento(arr):
    size = len(arr)
    funcion_sort(arr, size)

arr = []

print("Ingrese los 20 números:")
for datos in range(20):
    numeros = int(input())
    arr.append(numeros)

funcion_ordenamiento(arr)
print("Arreglo ordenado:", arr)
