import csv
from clase import ViajeroFrecuente


def leerDatos(archi):
    reader = csv.reader(archi, delimiter= ",")
    for fila in reader:
        unViajero = ViajeroFrecuente(0,0,"","",0)
        unViajero.leerDatos(fila)
        unViajero.mostrarDatos()
        lista.append(unViajero)
    print(len(lista))
    

def menu():
    print("""--------MENÚ DE OPCIONES--------
-1- Consultar Cantidad de Millas
-2- Acumular Millas
-3- Canjear Millas
-4- Buscar viajero con mayor cantidad de millas acumuladas
-5- Comparar cantidad de millas acumuladas POR IZQUIERDA
-6- Comparar cantidad de millas acumuladas POR DERECHA
-7- Acumular Millas POR DERECHA
-8- Canjear Millas POR DERECHA
-0- Salir""")
    x = int(input("Ingrese opcion: ")) #sin el cast por alguna razon me returna none en vez de 0, por lo que nunca sale
    return x


def buscoIndice(numIngresadoViajero): #BUSQUEDA SIEMPRE CON WHILE!!
    indice = 0
    i=0
    while indice == 0:
        resultado = lista[i].comparoNumeros(numIngresadoViajero)
        if resultado == 1:
            return i
        i +=1
    if resultado == -1:
        print("Numero ingresado incorrecto")
        return resultado

"""def buscoIndice(numIngresadoViajero):
    indice =0
    i=0
    while indice == 0:
        indice = lista[i].buscarObjeto(numIngresadoViajero)
        i += 1
    return indice"""
    
def viajerosMayores(mayor):
    for i in range(len(lista)):
        if mayor == lista[i].cantidadTotaldeMillas():
            lista[i].mostrarDatos()

def seleccion(opcion, indice):#------------switch del menu----------
    if opcion == 1:
        print(f"Usted tiene un total de {lista[indice].cantidadTotaldeMillas()} millas acumuladas") 
    elif opcion == 2:
        millasRecorridas = float(input("Ingrese la cantidad de millas recorridas: "))
        lista[indice] + millasRecorridas
        print("Millas añadidas")
    elif opcion == 3:
        millasAcanjear = float(input("Ingrese la cantidad de millas que desea canjear: "))
        if millasAcanjear <= lista[indice].cantidadTotaldeMillas():
            lista[indice] - millasAcanjear
            print("--Millas canjeadas!!--")
        else:
            return print("ERROR AL CANJEAR MILLAS")
    elif opcion == 4:
        mayor = -10000
        for i in range(len(lista)):
            if lista[i]>mayor:
                mayor = lista[i].cantidadTotaldeMillas()
        viajerosMayores(mayor)
    elif opcion == 5:
        millasAcomparar = int(input("Ingrese una cantidad a comparar: "))
        if lista[indice] == millasAcomparar:
            print("Cantidad de millas iguales")
        else: print("Las millas son distintas")
    elif opcion == 6:
        millasAcomparar = int(input("Ingrese una cantidad a comparar: "))
        if  millasAcomparar == lista[indice]:
            print("Cantidad de millas iguales")
        else: print("Las millas son distintas")
    elif opcion == 7:
        millasRecorridas = float(input("Ingrese la cantidad de millas recorridas: "))
        millasRecorridas + lista[indice]
        print("Millas añadidas")
    elif opcion == 8:
        millasAcanjear = float(input("Ingrese la cantidad de millas que desea canjear: "))
        if millasAcanjear <= lista[indice].cantidadTotaldeMillas():
            millasAcanjear - lista[indice]
            print("--Millas canjeadas!!--")
        else:
            return print("ERROR AL CANJEAR MILLAS")

if __name__ == '__main__':
    lista = []
    archi = open("aerolineas.csv")
    #------------Pto 1__LECTURA DE DATOS----------------
    leerDatos(archi)
    for i in range(len(lista)):
        print(i)
        lista[i].mostrarDatos()
    #------------Pto 2__MENU-------------
    #numViajeroFrec = input("Ingrese numero de viajero frecuente: ")
    opcion = -1
    indice = -1
    while indice == -1:#verifico numero de viajero ingresado
        numIngresadoViajero = int(input("Ingrese su numero de viajero frecuente: "))
        indice = buscoIndice(numIngresadoViajero) #Busco la instancia perteneciente al numero ingresado
    
    while opcion != 0:
        opcion = menu()
        seleccion(opcion, indice)
        if opcion == 0:
            print("SALIENDO...")
        