class Terminal:
    def __init__(self, valor):
        self.valor = valor
    def val(self):
        return self.valor
class NoTerminal: 
    def __init__(self, valor):
        self.valor = valor
    def val(self):
        return self.valor
class Estado: 
    def __init__(self, valor):
        self.valor = valor
    def val(self):
        return self.valor
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
liobj=["E"]
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
pilaobj=[]
pila.append("$")
pila.append(0)
pilaobj.append("$")
pilaobj.append(0)
cont=0
fila=pila[-1]
while cont < len(lisele):
    fila=pila[-1]
    columna=int(lisele[cont].get("num"))
    accion=(tablaej1[fila][columna])
    if (accion>0):
        pila.append(lisele[cont].get("num"))
        objeto1=NoTerminal(lisele[cont].get("lexema"))
        pilaobj.append(objeto1.val())
        objeto2=Estado(tablaej1[fila][columna])
        pila.append(tablaej1[fila][columna])
        pilaobj.append(objeto2.val())
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
            pilaobj.pop()
        fila=pila[-1]
        columna=li1[abs(accion)-2]
        pila.append(columna)
        objeto3=Terminal(liobj[columna-3])
        pilaobj.append(objeto3.val())
        pila.append(tablaej1[fila][columna])
        objeto3=Terminal(tablaej1[fila][columna])
        pilaobj.append(objeto3.val())
    print(pilaobj)
lisele.clear()
elementos=[]
entrada2="a+b+c+d+e+f"
lisele=analizadorLexico(entrada2)
for elemento in lisele:
    print(elemento)
pila.clear()
pilaobj.clear()
pila.append("$")
pila.append(0)
pilaobj.append("$")
pilaobj.append(0)
cont=0
fila=pila[-1]
while cont < len(lisele):
    fila=pila[-1]
    columna=int(lisele[cont].get("num"))
    accion=(tablaej2[fila][columna])
    if (accion>0):
        pila.append(lisele[cont].get("num"))
        objeto1=NoTerminal(lisele[cont].get("lexema"))
        pilaobj.append(objeto1.val())
        objeto2=Estado(tablaej2[fila][columna])
        pila.append(tablaej2[fila][columna])
        pilaobj.append(objeto2.val())
        cont+=1
    elif (accion==0):
        print("Cadena ejercicio 2 Inválida")
        break
    elif (accion==-1):
        print("Cadena ejercicio 2 Válida")
        break
    elif(accion<-1):
        if len(pila)<1:
            break
        for i in range (ld2[abs(accion)-2]*2):
            pila.pop()
            pilaobj.pop()
        fila=pila[-1]
        columna=li2[abs(accion)-2]
        pila.append(columna)
        objeto3=Terminal(liobj[columna-3])
        pilaobj.append(objeto3.val())
        pila.append(tablaej2[fila][columna])
        objeto3=Terminal(tablaej2[fila][columna])
        pilaobj.append(objeto3.val())
    print(pilaobj)
