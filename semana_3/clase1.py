from abc import ABC, abstractclassmethod

class ListaTDA(ABC):
    @abstractclassmethod
    def insertar(self, indice, elmento):
        """Insertar un elemento en una posicion especifica"""
        pass

    @abstractclassmethod
    def eliminar(self, indice):
        """Elimina y devuelve un elemento en una posicion especifica"""
        pass

    @abstractclassmethod
    def obtener(self, indice):
        """Obtiene un elemento en una posicion especifica"""
        pass

    @abstractclassmethod
    def esta_vacia(self):
        """Comprueba si la lista eta vacia """

        @abstractclassmethod
        def tamanio(self):
            """Obtiene el tamaño de la lista"""
            pass


            