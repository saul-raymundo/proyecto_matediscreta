import cv2
import glob
from pruebas import *

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
                            # El usuario ingresa, por ejemplo: 10, 20, 20, 30
                            conjunto1 = input("Ingresa los valores del concjunto 1: \n")
                            conjunto2 = input("Ingresa los valores del conjunto 2: \n")
                            resultad = opreac_conjunt(conjunto1,"union",conjunto2)
                            diseñotext("EL RESULTADO ES:",str(resultad),"*")
                            input()
                            diseñotext("DESEA","REGRESAR-S/N-","*")
                            back = input()
                            if back.lower() == "s":
                                diseñotext("1. A inicio"," 2.Menu opciones ","*")
                                dondereg = input()
                                activ2,activ1,activo = dondeir(dondereg)
                            elif back.lower() == "n":
                                activ2 = activ1 = activo = principal = False  
                        elif opcion == 2:

                            #para que ingrese los valores de los conjuntos
                            conjunto1 = input("Ingresa los valores del concjunto 1: \n")
                            conjunto2 = input("Ingresa los valores del conjunto 2: \n")
                            resultado = opreac_conjunt(conjunto1,"interseccion",conjunto2)
                            diseñotext("EL RESULTADO ES:",str(resultado),"*")

                            diseñotext("DESEA","REGRESAR-S/N-","*")
                            back = input()
                            if back.lower() == "s":
                                diseñotext("1. A inicio"," 2.Menu opciones ","*")
                                dondereg = input()
                                activ2,activ1,activo = dondeir(dondereg)
                            elif back.lower() == "n":
                                activ2 = activ1 = activo = principal = False  

                        elif opcion == 3:
                            #para que ingrese los valores de los conjuntos
                            conjunto1 = input("Ingresa los valores del concjunto 1: \n")
                            conjunto2 = input("Ingresa los valores del conjunto 2: \n")
                            resulta = opreac_conjunt(conjunto1,"diferencia",conjunto2)
                            diseñotext("EL RESULTADO ES:",str(resulta),"*")

                            diseñotext("DESEA","REGRESAR -S/N-","*")
                            back = input()
                            if back.lower() == "s":
                                diseñotext("1. A inicio"," 2.Menu opciones ","*")
                                dondereg = input()
                                activ2,activ1,activo = dondeir(dondereg)
                            elif back.lower() == "n":
                                activ2 = activ1 = activo = principal = False  

                        elif opcion == 4:
                            #para que ingrese los valores de los conjuntos
                            conjunto1 = input("Ingresa los valores del concjunto 1: \n")
                            conjunto2 = input("Ingresa los valores del conjunto 2: \n")
                            regist = opreac_conjunt(conjunto1,"complemento",conjunto2)
                            diseñotext("EL RESULTADO ES:",str(regist),"*")

                            diseñotext("DESEA","REGRESAR -S/N-","*")
                            back = input()
                            if back.lower() == "s":
                                diseñotext("1. A inicio"," 2.Menu opciones ","*")
                                dondereg = input()
                                activ2,activ1,activo = dondeir(dondereg)
                            elif back.lower() == "n":
                                activ2 = activ1 = activo = principal = False          

            elif opcionn == "3":
                #buscamos todas imagenes con .jpeg y creamos una lista con sus direcciones
                lista_imagen = glob.glob("*.jpeg")
                for ruta in lista_imagen:
                    imagen = cv2.imread(ruta)
                    if imagen is not None:
                        # Redimensionar para asegurar que quepa en la pantalla
                        imagen_redimensionada = cv2.resize(imagen, (400, 600))
                        cv2.imshow('INTEGRANTES GRUPO', imagen_redimensionada)
                        
                        # El programa se pausa aquí; presiona cualquier tecla para ver la siguiente foto
                        cv2.waitKey(0)

                # Cierra la ventana al terminar de recorrer toda la lista
                cv2.destroyAllWindows()
                input()
                diseñotext("DESEA","REGRESAR -S/N-","*")
                back = input()
                if back.lower() == "s":
                    diseñotext("1. A inicio"," 2.Menu opciones ","*")
                    dondereg = input()
                    activ2,activ1,activo = dondeir(dondereg)
                elif back.lower() == "n":
                                activ2 = activ1 = activo = principal = False
menuopcion("GRACIAS POR","EJECUTAR","NUESTRO","PROGRAMA","*")

                                
                    
        
    



       
       

        

