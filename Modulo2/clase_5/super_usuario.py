"""
Clase SuperUsuario hija de Administrador administrador.py
"""

from administrador import Administrador
from soporte import Soporte

class SuperUsuario(Administrador, Soporte):
     
    # Constructor

    def __init__(self, nombre, correo, activo, permisos):
            super().__init__(nombre, correo, activo)
            self.permisos = permisos

    # Metodos

    def presentarse(self):
        """ 
        Metodo que imprime por pantalla la presentacion del usuario y sus permisos
        """
        super().presentarse()
        print("Permisos:")
        for permiso in self.permisos:
            print(f"- {permiso}")
