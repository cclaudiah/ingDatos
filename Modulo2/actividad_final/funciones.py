"""Clase con las funciones necesarias para administrar la biblioteca"""
from libro import Libro
from usuario import Estudiante, Instructor
from prestamo import Prestamo

lista_libros = []
lista_usuario = []
lista_prestamo = []

def registrar_libro() :
    """Registra nuevo libro"""
    print("Registrar nuevo libro: \n")
    titulo = input("Título: ")
    autor = input("Autor: ")
    genero = input("Género: ")
    libro = Libro(titulo, autor, genero)
    lista_libros.append(libro)
    print("Libro registrado correctamente.")

def registrar_usuario() :
    """Registra nuevo usuario"""
    print("Registrar nuevo usuario: \n")
    nombre = input("Nombre: ")
    rol = input("Ingrese Rol: \n(E) Estudiante\n(I) Instructor: ")
    if rol.lower() == "i":
        usuario = Instructor(nombre)
    elif rol.lower() == "e":
        usuario = Estudiante(nombre)
    else :
        print("Opción incorrecta")
        return
    lista_usuario.append(usuario)
    print("Usuario registrado correctamente.")

def consultar_libro() :
    """ Segun las indicaciones de la actividad, se consulta solo por autor genero o disponibilidad y se agrega excepciones """

    try:
        print("Consultar libros: \nIngrese el criterio por el cual consultará")
        print("1.- Autor\n2.- Género\n3.- Disponibilidad")
        opc = int(input("Ingrese opción: "))
        filtro = input("Ingrese valor: ")
        if (len(lista_libros) == 0) :
            print("Debe registrar un libro primero")
            return
        else :
            libro_filtrado = buscar_libros(lista_libros, opc, filtro)
        
        if not libro_filtrado:
            raise ValueError("❌ No se encontraron libros con ese criterio.")
    except ValueError as ve:
        print(ve)
    except Exception as e:
        print(f"⚠️ Error inesperado: {e}")

def buscar_libros(lista_libros, opc, filtro):
    """Busca libro en lista_libros segun el filtro: autor, genero, disponibilidad """ 
    if opc == 1:
        print("filtro por Autor")
        for libro in lista_libros :
            if (libro.autor.lower() == filtro.lower()) :
                libro.info_libro()
                return libro
    
    elif opc == 2:
        print("filtro por Género")
        for libro in lista_libros :
            if (libro.genero.lower() == filtro.lower()) :
                libro.info_libro()
                return libro
    
    elif opc == 3:
        print("Libros Disponibles: ")
        for libro in lista_libros :
            if (libro.disponible is True) :
                libro.info_libro()
                return libro
    
    return []

def realizar_prestamo():
    """Realiza prestamo."""
    print("Prestar libro: ")
    try:
        print("Usuario a quien se prestará el libro")
        usuario_prestar = input("Nombre Usuario: ")
        if (len(lista_usuario) == 0) :
            print("Debe registrar usuarios primero")
            return
        else :
            libro_prestar = input("Nombre Libro: ")
            prestamo = ingresar_prestamo(lista_prestamo, usuario_prestar, libro_prestar)
        
        if not prestamo:
            raise ValueError("❌ No se realizó préstamo.")
    except ValueError as ve:
        print(ve)
    except Exception as e:
        print(f"⚠️ Error inesperado: {e}")

def ingresar_prestamo(lista_prestamo, usuario_prestar, libro_prestar):
    """ingresa dato a lista_prestamo""" 
    # primero busca que exista el usuario
    existe_usuario = False
    existe_libro = False
    existe_prestamo = False
    for usuario in lista_usuario :
        if (usuario.nombre.lower() == usuario_prestar.lower()) :
            existe_usuario = True
            break

    # si existe el usuario, busca que exista el libro
    if (existe_usuario) :   
        for libro in lista_libros :
            if (libro.titulo.lower() == libro_prestar.lower() and libro.disponible) :
                existe_libro = True
                break

    # si existe el libro y esta disponible, busca que no exista un prestamo
    if (existe_libro) :   
        for prestamo in lista_prestamo :
            if (prestamo.libro.titulo.lower() == libro_prestar.lower() and prestamo.usuario.nombre.lower() == usuario_prestar.lower()) :
                existe_prestamo = True
                break

    if not existe_usuario:
        raise ValueError("❌ Usuario no existe.")
    
    if not existe_libro:
        raise ValueError("❌ Libro no existe.")

    if existe_prestamo:
        raise ValueError("❌ Préstamo duplicado.")

    prestamo = Prestamo(usuario, libro)
    lista_prestamo.append(prestamo)
    libro.disponible = False
    print(f"📖 Préstamo registrado: {usuario.nombre} -> {libro.titulo}")
    return prestamo

def listar_prestados():
    """Lista los libros prestados."""
    print("Libros Prestados: ")
    for prestamo in lista_prestamo :
        print(f"\nUsuario: {prestamo.usuario.nombre} - Titulo: {prestamo.libro.titulo}.")
