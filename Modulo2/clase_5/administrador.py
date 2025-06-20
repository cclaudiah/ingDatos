"""
Clase Administrador hija de Usuario usuario.py
"""

from usuario import Usuario
from error_personalizado import PermisoInsuficienteError

class Administrador(Usuario):
     
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

    def agregar_permiso(self, permiso):
        if "administrador" not in self.permisos:
            raise PermisoInsuficienteError(
                f"{self.nombre} no posee el rol 'Administrador'"
             )
        if permiso not in self.permisos:
            self.permisos.append(permiso)
            print(f"Permiso agregado")