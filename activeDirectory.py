import csv
from os import system

class Directorio:
    

    def menu(self):
        i =1
        
        print('Elija la opcion deseada')
        print('Capturar persona........... (1)')
        print('Buscar Persona .............(2)')
        print('Modificar Persona ..........(4)')
        print('Eliminar Persona ...........(5)')
        print('Reporte de personas.........(6)')
        i = int(input('Opcion?, Zero para salir '))
        return(i)




    def AltaPersona(self):
        system('cls')
        a = []
        b = 1
        while(b==1):
            nombre = input('Captura nombre: ')
            apellido = input('Captura apellido: ')
            id = input('Captura id: ')
            a.append([nombre,apellido,id])
            archivo = open('directorio.csv','a')
            with archivo:
                escritor = csv.writer(archivo)
                escritor.writerows(a)
                print('Done')
            b = int(input('Capturar otro?, para salir presione cualquier, para continuar 1 '))

    def BuscaPersona(self):
        a=[]
        busqueda = input('Introduzca la clave de la persona: ')
        with open('directorio.csv', 'r') as archivo:
            lector = csv.reader(archivo)
            for renglon in lector:
                 if len(renglon)>0:
                    if renglon[2] == busqueda:
                        a.append(renglon)
                    
        return a








