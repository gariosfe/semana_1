class Node:
    def __init__(self, data):
        # Inicializa un nodo con el dato proporcionado y next apuntando a None
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        # Inicializa la pila con el atributo top apuntando a None
        self.top = None

    def push(self, item):
        # Crea un nuevo nodo con el dato proporcionado
        new_node = Node(item)
        # Establece el siguiente nodo del nuevo nodo al nodo que actualmente está en la cima de la pila
        new_node.next = self.top
        # Actualiza el atributo top para apuntar al nuevo nodo
        self.top = new_node

    def pop(self):
        # Verifica si la pila está vacía
        if self.is_empty():
            raise IndexError("pop from empty stack")
        # Guarda el dato del nodo superior en una variable
        data = self.top.data
        # Actualiza el atributo top para apuntar al siguiente nodo
        self.top = self.top.next
        # Devuelve el dato guardado
        return data

    def is_empty(self):
        # Verifica si la pila está vacía
        return self.top is None

def reverse_text(text):
    # Crea una instancia de la clase Stack
    stack = Stack()
    # Itera sobre cada caracter en la cadena de texto
    for char in text:
        # Añade cada caracter a la pila
        stack.push(char)

    # Inicializa una cadena vacía para almacenar el texto invertido
    reversed_text = ""
    # Continúa sacando caracteres de la pila y concatenándolos a la cadena invertida
    while not stack.is_empty():
        reversed_text += stack.pop()

    # Devuelve la cadena invertida
    return reversed_text

# Ejemplo de uso de la aplicación de reversión de texto
if __name__ == "__main__":
    text = "Hola mundo!"
    reversed_text = reverse_text(text)
    print(f"Texto original: {text}")
    print(f"Texto invertido: {reversed_text}")