# Clase Nodo que representa cada nodo en la lista doblemente enlazada
class Nodo:
    def __init__(self, dato=None):
        # Inicializa el nodo con un dato, y los punteros siguiente y anterior
        self.dato = dato
        self.siguiente = None
        self.anterior = None
# Clase que representa la lista doblemente enlazada
class ListaDoblementeEnlazada:
    def __init__(self):
        # Inicializa la lista con cabeza, cola y cursor vacíos
        self.cabeza = None
        self.cola = None
        self.cursor = None

    # Método para insertar un nuevo nodo en la lista
    def insertar(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.cabeza is None:
            # Si la lista está vacía, el nuevo nodo es la cabeza y la cola
            self.cabeza = self.cola = nuevo_nodo
        else:
            # Añade el nuevo nodo al final de la lista
            nuevo_nodo.anterior = self.cola
            self.cola.siguiente = nuevo_nodo
            self.cola = nuevo_nodo
        if self.cursor is None:
            # Si el cursor está vacío, lo posiciona en la cabeza
            self.cursor = self.cabeza

    # Método para eliminar el nodo en la posición del cursor
    def eliminar(self):
        if self.cursor is None:
            return  # Si el cursor está vacío, no hay nada que eliminar
        if self.cursor == self.cabeza and self.cursor == self.cola:
            # Si el cursor es el único nodo, la lista queda vacía
            self.cabeza = self.cola = None
        elif self.cursor == self.cabeza:
            # Si el cursor está en la cabeza, mueve la cabeza al siguiente nodo
            self.cabeza = self.cabeza.siguiente
            self.cabeza.anterior = None
        elif self.cursor == self.cola:
            # Si el cursor está en la cola, mueve la cola al nodo anterior
            self.cola = self.cola.anterior
            self.cola.siguiente = None
        else:
            # Si el cursor está en el medio, ajusta los punteros de los nodos adyacentes
            self.cursor.anterior.siguiente = self.cursor.siguiente
            self.cursor.siguiente.anterior = self.cursor.anterior
        # Mueve el cursor al siguiente nodo o a la cola si no hay siguiente
        self.cursor = self.cursor.siguiente if self.cursor.siguiente else self.cola

    # Método para mover el cursor a la derecha
    def mover_cursor_derecha(self):
        if self.cursor and self.cursor.siguiente:
            self.cursor = self.cursor.siguiente

    # Método para mover el cursor a la izquierda
    def mover_cursor_izquierda(self):
        if self.cursor and self.cursor.anterior:
            self.cursor = self.cursor.anterior

    # Método para obtener el texto completo de la lista
    def obtener_texto(self):
        texto = []
        nodo_actual = self.cabeza
        while nodo_actual:
            # Recorre la lista y añade cada dato a la lista de texto
            texto.append(nodo_actual.dato)
            nodo_actual = nodo_actual.siguiente
        return ''.join(texto)  # Une los caracteres en un solo string

    # Método para representar la lista como una cadena de texto
    def __str__(self):
        return self.obtener_texto()

# Clase que implementa el editor de texto simple usando la lista doblemente enlazada
class EditorTextoSimple:
    def __init__(self):
        self.lista = ListaDoblementeEnlazada()  # Crea una instancia de la lista

    # Método para insertar un carácter en la lista
    def insertar(self, caracter):
        self.lista.insertar(caracter)

    # Método para eliminar el carácter en la posición del cursor
    def eliminar(self):
        self.lista.eliminar()

    # Método para mover el cursor a la derecha
    def mover_cursor_derecha(self):
        self.lista.mover_cursor_derecha()

    # Método para mover el cursor a la izquierda
    def mover_cursor_izquierda(self):
        self.lista.mover_cursor_izquierda()

    # Método para mostrar el texto completo de la lista
    def mostrar_texto(self):
        print(self.lista)

# Pruebas del editor de texto

editor = EditorTextoSimple()

# Insertando caracteres
editor.insertar('H')
editor.insertar('o')
editor.insertar('l')
editor.insertar('a')
editor.insertar(' ')
editor.insertar('M')
editor.insertar('u')
editor.insertar('n')
editor.insertar('d')
editor.insertar('o')

# Mostrando el texto
editor.mostrar_texto()  # Hola Mundo

# Moviendo el cursor a la izquierda y eliminando un carácter
editor.mover_cursor_izquierda()
editor.mover_cursor_izquierda()
editor.eliminar()

# Mostrando el texto
editor.mostrar_texto()  # Hola Mudo

# Insertando un nuevo carácter
editor.insertar('n')

# Mostrando el texto final
editor.mostrar_texto()  # Hola Mundo
