"Clase Libro"

class Libro:
     
    # Constructor

    def __init__(self, titulo, autor, genero):
            self.titulo = titulo
            self.autor = autor
            self.genero = genero
            self.disponible = True

    # Metodos

    def info_libro(self):
        """
        Metodo que imprime por pantalla los datos del libro.
        """
        print(f"\nTitulo: {self.titulo} \nAutor {self.autor} \nGénero {self.genero}.")