elementos=[]
def analizadorLexico(cadena):
    if not cadena:
        return print("Cadena vacia")
    if cadena[-1]!='$':cadena=cadena+'$'
    indice=0
    estado=-1
    while(indice<=(len(cadena)-1)  and estado==-1):  
            lexema=''
            token='error'
            num=0
            while(indice<=(len(cadena)-1) and estado!=2):
                if estado==-1:
                    if(cadena[indice].isspace()):
                        estado=-1
                    elif cadena[indice].isalpha() or cadena[indice]=='_':
                        estado=0
                        lexema+=cadena[indice]
                        token='id'
                        num=0
                    elif cadena[indice]=='$':
                        estado=2
                        lexema+=cadena[indice]
                        token='pesos'
                        num=2
                    elif cadena[indice]=='+' or cadena[indice]=='-':
                        lexema+=cadena[indice]
                        token='opSuma'
                        estado=2
                        num=1
                    indice+=1
                elif estado==0:
                    if cadena[indice].isdigit() or cadena[indice].isalpha() or cadena[indice]=='_':
                        estado=0
                        lexema+=cadena[indice]
                        token='id'
                        indice+=1
                        num=0
                    else:
                        estado=2
            estado=-1
            elementos.append({'token':token,'lexema':lexema, 'num':num})
    return elementos
entrada="hola+mundo"
lisele=analizadorLexico(entrada)
for elemento in lisele:
    print(elemento)
ld1=[3]
li1=[3]
ld2=[3,1]
li2=[3,3]
tablaej1=[[2,0,0,1],
       [0,0,-1,0],
       [0,3,0,0],
       [4,0,0,0],
       [0,0,-2,0]]
tablaej2=[[2,0,0,1],
       [0,0,-1,0],
       [0,3,-3,0],
       [2,0,0,4],
       [0,0,-2,0]]
pila=[]
pila.append("$")
pila.append(0)
cont=0
fila=pila[-1]
while cont < len(lisele):
    fila=pila[-1]
    columna=int(lisele[cont].get("num"))
    accion=(tablaej1[fila][columna])
    if (accion>0):
        pila.append(lisele[cont].get("num"))
        pila.append(tablaej1[fila][columna])
        cont+=1
    elif (accion==0):
        print("Cadena ejercicio 1 Inválida")
        break
    elif (accion==-1):
        print("Cadena ejercicio 1 Válida")
        break
    elif(accion<-1):
        if len(pila)<1:
            break
        for i in range (ld1[abs(accion)-2]*2):
            pila.pop()
        fila=pila[-1]
        columna=li1[abs(accion)-2]
        pila.append(columna)
        pila.append(tablaej1[fila][columna])
    print(pila)
elementos=[]
entrada2="a+b+c+d+e+f"
lisele2=analizadorLexico(entrada2)
for elemento in lisele2:
    print(elemento)
pila2=[]
pila2.append("$")
pila2.append(0)
cont=0
fila2=pila2[-1]
while cont < len(lisele2):
    fila2=pila2[-1]
    columna2=int(lisele2[cont].get("num"))
    accion=(tablaej2[fila2][columna2])
    if (accion>0):
        pila2.append(lisele2[cont].get("num"))
        pila2.append(tablaej2[fila2][columna2])
        cont+=1
    elif (accion==0):
        print("Cadena ejercicio 2 Inválida")
        break
    elif (accion==-1):
        print("Cadena ejercicio 2 Válida")
        break
    elif(accion<-1):
        if len(pila2)<1:
            break
        for i in range (ld2[abs(accion)-2]*2):
            pila2.pop()
        fila2=pila2[-1]
        columna2=li2[abs(accion)-2]
        pila2.append(columna2)
        pila2.append(tablaej2[fila2][columna2])
    print(pila2)
