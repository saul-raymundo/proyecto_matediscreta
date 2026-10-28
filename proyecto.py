import cv2
import glob
from pruebas import *
#buscamos todos los balores de imagenes con .jpg
lista_imagen = glob.glob("*.jpg")

conjuntA = {}
conjuntB={}
universal = {}
principal = True
while principal:
    activo=activ1 = True
    while activo:
        diseñotext("Trinomio","bienvenidos","*")
        input()
        while activ1:
            menu_principal(" MENU DE OPCIONES ","1-INICIO","2-CONJUNTOS","3-SOBRE NOSOTROS","*")
            opcionn = input()
            if opcionn == "1":
                break
            elif opcionn =="2":
                    activ2 = True
                    while activ2:
                        #menu opciones de conjuntos
                        menuopcion("1-Union","2-Interseccion","3-Diferencia","4-complemento","*")
                        opcion = int(input())
                        if opcion == 1:
                            #para que ingrese los valores de los conjuntos
                            
                            print("desea regresar S/N: ")
                            back = input()
                            if back.lower() == "s":
                                diseñotext("1. A inicio"," 2.Menu opciones ","*")
                                dondereg = input()
                                if dondereg == "1":
                                    activ2 = False
                                    activ1 = False 
                                    activo = False
                                elif dondereg == "2":
                                    activ2 = False 
                                else:
                                    print("ERROR tienes que decidir a donde ir")
                            elif back.lower() == "n":
                                activ2 = False,activ1 = False , activo = False,principal = False  
                        elif opcion == 2:
                            
                    
        
    



       
       

        

