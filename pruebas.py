def diseñotext(text1,text2,marco):
    arrib = (marco.ljust(50,marco))#son los marcos de arriba
    i = 0
    print(arrib)
    while True:
        forma = (marco+ " " * 49 + marco)#esta agrega los "*" a los costados mientras tiene 49 espacios dentro
        print(forma)
        i +=1
        if i == 1:#siginifica que luego de dos lineas de espacios con asterisco se ejecuta lo siguiente
            inf = text1.center(47)
            inf2 = text2.center(47)
            print(marco,inf,marco)
            print(marco,inf2,marco)
            print(forma+'\n'+ arrib)#aca agrega dos enter y luego muestra el marco de abajo del recuadro
            break

def menu_principal(tex1,tex2,tex3,tex4,mards):
    arrib_ab = (mards.ljust(50,mards))
    print(arrib_ab)
    i = 0
    while True:
        forma = (mards+ " " * 49 + mards)#esta agrega los "*" a los costados mientras tiene 49 espacios dentro
        print(forma)
        i +=1
        if i == 1:#siginifica que luego de dos lineas de espacios con asterisco se ejecuta lo siguiente
            inf = tex1.center(47)
            inf2 = tex2.center(47)
            inf3 = tex3.center(47)
            inf4 = tex4.center(47)
        print(mards,inf,mards)
        print(mards,inf2,mards)
        print(mards,inf3,mards)
        print(mards,inf4,mards)
        print(forma+'\n'+ arrib_ab)#aca agrega dos enter y luego muestra el marco de abajo del recuadro
        break

def menuopcion(tex1,text2,tex3,tex4,marcs):
    arrib_ab = (marcs.ljust(50,marcs))#son los marcos de arriba
    print(arrib_ab)
    i = 0
    while True:
            forma = (marcs+ " " * 49 + marcs)#esta agrega los "*" a los costados mientras tiene 49 espacios dentro
            print(forma)
            i +=1
            if i == 1:#siginifica que luego de dos lineas de espacios con asterisco se ejecuta lo siguiente
                inf = tex1.center(47)
                inf2 = text2.center(47)
                inf3 = tex3.center(47)
                inf4 = tex4.center(47)

                print(marcs,inf,marcs)
                print(marcs,inf2,marcs)
                print(marcs,inf3,marcs)
                print(marcs,inf4,marcs)
                print(forma+'\n'+ arrib_ab)#aca agrega dos enter y luego muestra el marco de abajo del recuadro
                break

def dondeir(quedicid):
    if quedicid == "1":
        
        return False,False,False
    elif quedicid == "2":
        return False,True,True
    else:
        return "ERROR tienes que decidir a donde ir"

    
def opreac_conjunt(conjunt1,opreacion,conjunt2):
    if opreacion == "union":
        # Separamos el texto, convertimos a enteros (int) y creamos el conjunto
        conjunto_1 = set([int(x) for x in conjunt1.split(",")])
        conjunto_2 = set([int(x) for x in conjunt2.split(",")])
        union = conjunto_1 | conjunto_2
        return union
    elif opreacion == "iterseccion":
        conjunto_i = set([int(x) for x in conjunt1.split(",")])
        conjunto_i2 = set([int(x) for x in conjunt2.split(",")])
        interseccion = conjunto_i & conjunto_i2
        return interseccion
    elif opreacion == "diferencia":
        conju_d1 = set([int(x) for x in conjunt1.split(",")])
        conj_d2 = set([int(x) for x in conjunt2.split(",")])
        diferencia = conju_d1 - conj_d2
        return diferencia
    elif opreacion == "complemento":
        conj_universal = set([int(x) for x in conjunt1.split(",")])
        conj_A = set([int(x) for x in conjunt2.split(",")])
        complemento = conj_universal - conj_A
        return complemento



   
    