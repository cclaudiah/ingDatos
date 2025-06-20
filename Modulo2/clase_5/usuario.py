"""
Clase Usuario
"""
class Usuario:
     
    # Constructor

    def __init__(self, nombre, correo, activo=True):
            self.nombre = nombre
            self.correo = correo
            self.activo = activo

    # Metodos

    def presentarse(self):
        """
        Metodo que imprime por pantalla la presentacion del usuario.
        """
        print(f"\nHola, soy {self.nombre}, mi correo es {self.correo} y mi estado es {self.activo}.")