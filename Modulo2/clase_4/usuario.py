"""
Clase Usuario
"""
class Usuario:
     
    # Constructor

    def __init__(self, nombre, correo, contrasena):
            self.nombre = nombre
            self.correo = correo
            self._contrasena = contrasena

    # Metodos

    def saludar(self):
        """ 
        Metodo que imprime por pantalla el saludo con el correo usuario
        """
        print(f"Hola {self.nombre}, Bienvenida al curso de Ing. de Datos.")
        print("Módulo 2 - Clase 4")
        print("")

    def mostrar_info(self):
        """ 
        Metodo que imprime los datos del usuario
        """
        print(f"Nombre: {self.nombre}")
        print(f"Correo: {self.correo}")
        print(f"Contraseña actual: {self._contrasena}")


    # Getters y setters

    @property
    def contrasena(self):
        return self._contrasena

    @contrasena.setter
    def contrasena(self, nueva_contrasena):
        self._contrasena = nueva_contrasena