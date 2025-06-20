"""
Clase Cliente hija de Usuario usuario.py
"""

from usuario import Usuario

class Cliente(Usuario):
     
    # Constructor

    def __init__(self, nombre, correo, contrasena, tipo_cliente):
            super().__init__(nombre, correo, tipo_cliente)
            self.tipo_cliente = tipo_cliente

    # Metodos

    def saludar(self):
        """ 
        Metodo que imprime por pantalla la clase los datos de la clase hija, llamando al metodo mostrar_info de la clase padre
        """
        print("Clase cliente, hija de usuario")
        super().mostrar_info()
        print(f"tipo cliente: {self.tipo_cliente}")
