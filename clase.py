import re

class ViajeroFrecuente:
    __numViajero = int
    __DNI = float
    __nombre = str
    __apellido = str
    __millasAcum = float

    def __init__(self, numViajero, DNI, nombre, apellido, millasAcum):
        self.__numViajero = numViajero
        self.__DNI = DNI
        self.__nombre = nombre
        self.__apellido = apellido
        self.__millasAcum = millasAcum

    def leerDatos(self, datoViajero):
        self.__numViajero = int(datoViajero[0])
        self.__DNI = datoViajero[1]
        self.__nombre = datoViajero[2]
        self.__apellido = datoViajero[3]
        self.__millasAcum = float(datoViajero[4]) #tengo que meter un cast porque me lo guarda como string y luego tira error al sumar las millas

    def cantidadTotaldeMillas(self):
        return self.__millasAcum
    
    def mostrarDatos(self):
        print(f"Numero de viajero: {self.__numViajero}\nDNI: {self.__DNI}\nNombre: {self.__nombre}\nApellido: {self.__apellido}\nMillas acumuladas: {self.__millasAcum}\n")

    #def cantidadTotaldeMillas(self):
    
    def comparoNumeros(self, numIngresadoViajero):#veo si coinciden los numeros de viajero
        if self.__numViajero == numIngresadoViajero:
            return 1
        else:
            return -1

    """def acumularMillas(self, millasRecorridas):
        self.__millasAcum += millasRecorridas

    -----REEMPLAZADO POR SOBRECARGA ADD----"""

    """def canjearMillas(self, millasAcanjear):
        if millasAcanjear <= self.__millasAcum:
            self.__millasAcum -= millasAcanjear
            return self.__millasAcum
        else:
            return print("ERROR AL CANJEAR MILLAS")
            ---REEMPLAZADO POR SOBRECARGA SUB----"""
  
    """def buscarObjeto(self, numIngresadoViajero):
        indice =0
        indice = self.index(numIngresadoViajero)
        return indice"""
    
    def __gt__(self, mayor):
        return self.__millasAcum > mayor
    
    def __add__(self, cantidad):
        self.__millasAcum += cantidad
        return self.__millasAcum
    
    def __sub__(self, cantidad):
        self.__millasAcum -= cantidad
        return self.__millasAcum
    
    def __eq__(self, cantidad):
        return self.__millasAcum == cantidad
    
    """def __req__(self, cantidad):
        print("-----------ENTRO POR DERECHA-------------")
        return self.__millasAcum == cantidad"""

    def __rsub__(self, cantidad):
        print("-----------ENTRO POR DERECHA-------------")
        self.__millasAcum -= cantidad
        return self.__millasAcum
    
    def __radd__(self, cantidad):
        print("-----------ENTRO POR DERECHA-------------")
        self.__millasAcum += cantidad
        return self.__millasAcum