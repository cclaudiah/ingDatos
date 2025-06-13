"""
    operaciones.py

    Codigo con funciones matematicas del ejercicio de la clase 2
"""

def sumar(a, b):
    """ 
    Funcion que retorna la suma de dos numeros
    
    Parametros
    a: int
    b: int

    Return: resultado de la suma
    """

    return a + b

def restar(a, b=5):
    """
    Funcion que retorna la resta de dos numeros.
    
    Parametros
    a: int
    b: int toma el valor de 5 si es que el valor no es ingresado

    Return: resultado de la resta
    """
    return a - b

def multiplicar(*args):
    """
    Funcion que retorna el producto de la multiplicacion
    
    Parametros
    *args: int

    Return: producto
    """
    resultado = 1
    for i in args:
        resultado = resultado * i
    return resultado

def mostrar_info(**kwargs):
    """
    Funcion que despliega por pantalla los parametros ingresados.

    Parametros
    **kwargs : clave, valor
    """
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")

potencia = lambda base, exponente: base ** exponente

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)