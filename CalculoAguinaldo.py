'''
@Kevin Alexander Peña Sanchez
@kpsystemout@clases.edu.sv
Desarrolle un script en el cual el usuario (contador de una empresa) pueda introducir los siguientes datos:

-Nombre del empleado
-DUI del empleado
-NIT del empleado
-Sueldo neto del empleado
-Tiempo que el empleado lleva trabajando en la empresa (usted puede elegir si el usuario debe digitar años, meses o días)

'''
def Datos():
    """Función para solicitar los datos del usuario"""

    
    print("""-----------------------------------------------------------------------------------------------------------
|                                        CALCULADORA DE AGUINALDO                                         |
-----------------------------------------------------------------------------------------------------------\n""")

    nombre = input("Ingrese su nombre completo: ")

    dui = input("Ingrese su número de DUI (SIN GUIONES): ")

    #Verifica que el DUI tenga una longitud válida
    while(len(dui) != 9):
        print("¡El número de DUI no es válido!")
        dui = input("Ingrese nuevamente su número de DUI (SIN GUIONES): ")

    #Lambda que permite dar formato al número del DUI
    dui_real = lambda dui: dui[:-1] + "-" + dui[-1]

    #----NIT----
    nit = input("Ingrese su número de NIT (SIN GUIONES): ")

    #Verifica que el NIT tenga una longitud válida
    while(len(nit) != 14):
        print("¡El número de NIT no es válido!")
        nit = input("Ingrese nuevamente su número de NIT (SIN GUIONES): ")

    #Lambda que permite dar formato al número del NIT
    nit_real = lambda nit: nit[:4] + "-" + nit[4:10] + "-" + nit[10:13] + "-" + nit[-1] #lambda que permite dar formato al número del NIT

    salario = float(input("Ingrese su sueldo: $"))
    tiempo = int(input("Ingrese el número de meses trabajados: "))

    return nombre, dui, dui_real, nit, nit_real, salario, tiempo #Devuelve las variables a utilizar

class Calculo():

    #Constructor
    def __init__(self, nombre, dui, nit,salario,tiempo):
        self.nombre = nombre
        self.dui = dui
        self.nit = nit
        self.salario = salario
        self.tiempo = tiempo
        self.aguinaldo = 0

    #Calcula el aguinaldo
    def calcular(self):
        if self.tiempo >= 12 and self.tiempo < 36:
            self.aguinaldo = (self.salario/30)*15
        elif self.tiempo >= 36 and self.tiempo <120:
            self.aguinaldo = (self.salario/30)*19
        elif self.tiempo >= 120:
            self.aguinaldo = (self.salario/30)*21
        else:
            self.aguinaldo = (((self.salario/30)*15)/365 * 30*self.tiempo)
 
    def imprimir(self):
        print("""|---------------------------------------------------------------------------------------------------------|
|                                                RESULTADOS                                               |
|---------------------------------------------------------------------------------------------------------|\n""")
        print("Nombre: " + self.nombre.title() + "\nDUI: " + self.dui + "\nNIT: " + self.nit)
        print("Tiempo laborado: " + str(self.tiempo) + " meses ("+ str(round(self.tiempo/12,2)) +" años)\nSalario: $" + str(self.salario))
        print("""\n|---------------------------------------------------------------------------------------------------------|
|---------------------------------------------------------------------------------------------------------|\n""")
        print("El aguinaldo a recibir es de: $" + str(round(self.aguinaldo,3)))

from os import system, name #Nos permitirá limpiar la pantalla en un futuro

def limpiar():
    """Limpia la pantalla de la terminal"""
    if name == 'nt': #Evalúa si se encuentra en un sistema operativo Windows
        _ = system('cls')
    else: #Si se encuentra en Mac o Linux
        _ = system('clear')


#Declaración de variables
nombre, dui, dui_real, nit, nit_real, salario, tiempo = Datos() 

limpiar() #Nos permite limpiar la terminal. Se utiliza para presentar de manera ordenada los datos.

#Instancia de clase Calculo
mi_aguinaldo = Calculo(nombre,str(dui_real(dui)),str(nit_real(nit)),salario, tiempo) 
mi_aguinaldo.calcular() #Calcula el aguinaldo
mi_aguinaldo.imprimir() #Imprime los resultados

#Si se abre desde el ejecutable, evita que se cierre sin haber mostrado resultados
input("\n\n\nFIN DE LA EJECUCION -- Presione cualquier tecla para salir")
