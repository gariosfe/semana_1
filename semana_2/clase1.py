def funcion_duble(arr):
    n = len(arr) 

    for i in range(n): 
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]



def funcion_sort(arr, size):
    for d in range(size):
        min_indi = d  
    
        for i in range(d + 1, size):
            if arr[i] < arr[min_indi]:
                min_indi = i  

        arr[d], arr[min_indi] = arr[min_indi], arr[d]  


def funcion_ordenamiento(arr):


    
arr = []

for datos in range(20):
    numeros = int(input())
    arr.append(numeros)
print("Ingrese los 20 numeros: " )