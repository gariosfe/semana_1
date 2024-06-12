class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def añadir(self, valor):
        nuevo_nodo = Nodo(valor)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def eliminar(self, valor):
        actual = self.cabeza
        previo = None
        while actual and actual.valor != valor:
            previo = actual
            actual = actual.siguiente
        if not actual:
            return False
        if not previo:
            self.cabeza = actual.siguiente
        else:
            previo.siguiente = actual.siguiente
        return True

    def mostrar(self):
        elementos = []
        actual = self.cabeza
        while actual:
            elementos.append(actual.valor)
            actual = actual.siguiente
        return elementos

    
class Playlist:
    def __init__(self):
        self.lista = ListaEnlazada()

    def añadir_cancion(self, cancion):
        self.lista.añadir(cancion)
        print(f"Canción '{cancion}' añadida a la playlist.")

    def eliminar_cancion(self, cancion):
        if self.lista.eliminar(cancion):
            print(f"Canción '{cancion}' eliminada de la playlist.")
        else:
            print(f"Canción '{cancion}' no encontrada en la playlist.")

    def mostrar_playlist(self):
        canciones = self.lista.mostrar()
        if canciones:
            print("Playlist actual:")
            for idx, cancion in enumerate(canciones, 1):
                print(f"{idx}. {cancion}")
        else:
            print("La playlist está vacía.")

    def buscar_cancion(self, cancion):
        actual = self.lista.cabeza
        while actual:
            if actual.valor == cancion:
                print(f"Canción '{cancion}' encontrada en la playlist.")
                return True
            actual = actual.siguiente
        print(f"Canción '{cancion}' no encontrada en la playlist.")
        return False

    def reorganizar_playlist(self, cancion, nueva_posicion):
        # Eliminar la canción
        if not self.lista.eliminar(cancion):
            print(f"Canción '{cancion}' no encontrada en la playlist.")
            return
        # Añadir en la nueva posición
        self.añadir_en_posicion(cancion, nueva_posicion)
        print(f"Canción '{cancion}' movida a la posición {nueva_posicion}.")

    def añadir_en_posicion(self, valor, posicion):
        nuevo_nodo = Nodo(valor)
        if posicion == 1:
            nuevo_nodo.siguiente = self.lista.cabeza
            self.lista.cabeza = nuevo_nodo
        else:
            actual = self.lista.cabeza
            previo = None
            actual_pos = 1
            while actual and actual_pos < posicion:
                previo = actual
                actual = actual.siguiente
                actual_pos += 1
            if previo:
                previo.siguiente = nuevo_nodo
                nuevo_nodo.siguiente = actual
    

# Crear instancia de Playlist
mi_playlist = Playlist()

# Añadir canciones
mi_playlist.añadir_cancion("Song 1")
mi_playlist.añadir_cancion("Song 2")
mi_playlist.añadir_cancion("Song 3")

# Mostrar playlist
mi_playlist.mostrar_playlist()

# Buscar una canción
mi_playlist.buscar_cancion("Song 2")

# Eliminar una canción
mi_playlist.eliminar_cancion("Song 2")

# Mostrar playlist nuevamente
mi_playlist.mostrar_playlist()

# Reorganizar la playlist
mi_playlist.reorganizar_playlist("Song 3", 1)

# Mostrar playlist final
mi_playlist.mostrar_playlist()


