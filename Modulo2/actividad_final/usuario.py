"Clase Usuario"
# Se especifica en el ejercicio crear clases hijas Estudiante y Instructor

class Usuario:
     
    # Constructor

    def __init__(self, nombre):
            self.nombre = nombre
            # self.rol = rol

class Estudiante(Usuario):
    """Rol Estudiante."""
    def tipo(self):
        return "Estudiante"


class Instructor(Usuario):
    """Rol Instructor."""
    def tipo(self):
        return "Instructor"