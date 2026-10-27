import cv2
import glob
from pruebas import *
#buscamos todos los balores de imagenes con .jpg
lista_imagen = glob.glob("*.jpg")

conjuntA = {}
conjuntB={}
universal = {}
while True:
    diseñotext("Trinomio","bienvenidos","*")
    input()
    while True:
        #menu opciones
        menuopcion("1-Union","2-Interseccion","3-Diferencia","4-complemento","*")
        opcion = int(input())
        if opcion == 1:
            print("ingresa valor")
            print("desea regresar S/N: ")
            back = input()
            if back == "s":
                diseñotext("1. A inicio"," 2.Menu ","*")
                dondereg = input()
                if dondereg == "1":
                    break
                
        elif opcion == 2:
            print("opcion tho")
        elif opcion == 3:
            print( "opcione three")
        elif opcion == 4:
            print("opcion fourd")
        elif opcion == None:
            print("elije una opcion porfavor")

        

