# Reversión de Texto utilizando una Pila

Este es un ejemplo de implementación de una pila en Python y su aplicación para revertir una cadena de texto.

## Clase Node

La clase `Node` representa un nodo en una estructura de datos enlazada. Cada nodo contiene un dato y una referencia al siguiente nodo.

- `__init__(self, data)`: Inicializa un nodo con el dato proporcionado y `next` apuntando a `None`.

## Clase Stack

La clase `Stack` implementa una pila utilizando una estructura de datos enlazada.

- `__init__(self)`: Inicializa la pila con el atributo `top` apuntando a `None`.
- `push(self, item)`: Añade un nuevo elemento a la pila. Crea un nuevo nodo con el dato proporcionado y lo coloca en la cima de la pila.
- `pop(self)`: Elimina y devuelve el elemento en la cima de la pila. Verifica si la pila está vacía antes de hacer `pop`.
- `is_empty(self)`: Verifica si la pila está vacía.

## Función reverse_text

La función `reverse_text(text)` toma una cadena de texto como entrada y utiliza una pila para invertirla.

- Crea una instancia de la clase `Stack`.
- Itera sobre cada caracter en la cadena de texto y los añade a la pila.
- Inicializa una cadena vacía para almacenar el texto invertido.
- Continúa sacando caracteres de la pila y concatenándolos a la cadena invertida hasta que la pila esté vacía.
- Devuelve la cadena invertida.

## Ejemplo de Uso

```python
if __name__ == "__main__":
    text = "Hola mundo!"
    reversed_text = reverse_text(text)
    print(f"Texto original: {text}")
    print(f"Texto invertido: {reversed_text}")

