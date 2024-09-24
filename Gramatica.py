from cgitb import text
from tkinter import *
import pandas as pd
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
tabla = pd.read_csv('Tabla.txt', sep='\t', header=None,engine='python')
top=Tk()
top.geometry("805x500")
top.configure(bg="light gray")
top.title('Gramática del compilador')
elementos=[]
entrada="cadena a analizar"
def analizadorLexico(cadena):
    decim=False
    if cadena[-1]!='$':cadena=cadena+'$'
    indice=0
    estado=-1
    while(indice<=(len(cadena)-1)  and estado==-1):  
            lexema=''
            token='error'
            num=0
            while(indice<=(len(cadena)-1) and estado!=23):
                if estado==-1:
                    if(cadena[indice].isspace()):
                        estado=-1
                    elif cadena[indice].isalpha() or cadena[indice]=='_':
                        estado=0
                        lexema+=cadena[indice]
                        token='id'
                        num=0
                    elif cadena[indice]=='$':
                        estado=23
                        lexema+=cadena[indice]
                        token='pesos'
                        num=23
                    elif cadena[indice]=='=':
                        lexema+=cadena[indice]
                        token='asignación'
                        estado=18
                        num=18
                    elif cadena[indice]==';':
                        lexema+=cadena[indice]
                        token='punto y coma'
                        estado=23 
                        num=12
                    elif cadena[indice]==',':
                        lexema+=cadena[indice]
                        token='coma'
                        estado=23
                        num=13
                    elif cadena[indice]=='(':
                        lexema+=cadena[indice]
                        token='parentesis abierto'
                        estado=23
                        num=14
                    elif cadena[indice]==')':
                        lexema+=cadena[indice]
                        token='parentesis cerrado'
                        estado=23
                        num=15
                    elif cadena[indice]=='{':
                        lexema+=cadena[indice]
                        token='corchete abierto'
                        estado=23
                        num=16
                    elif cadena[indice]=='}':
                        lexema+=cadena[indice]
                        token='corchete cerrado'
                        estado=23  
                        num=17
                    elif cadena[indice].isdigit():
                        estado=1
                        lexema+=cadena[indice]
                        token='entero'
                        num=1
                    elif cadena[indice]=='+' or cadena[indice]=='-':
                        lexema+=cadena[indice]
                        token='opSuma'
                        estado=23 
                        num=5
                    elif cadena[indice]=='|' or cadena[indice]=='&':
                        lexema+=cadena[indice]
                        estado=8
                    elif cadena[indice]=='*' or cadena[indice]=='/':
                        lexema+=cadena[indice]
                        token='opMultiplicacion'
                        estado=23   
                        num=6
                    elif cadena[indice]=='<':
                        lexema+=cadena[indice]
                        token='opRelacional'
                        estado=7   
                        num=7
                    elif cadena[indice]=='>':
                        lexema+=cadena[indice]
                        token='opRelacional'
                        estado=23   
                        num=7
                    elif cadena[indice]=='!':
                        lexema+=cadena[indice]
                        token='opNot'
                        estado=7
                        num=10 
                    else:
                        estado=23
                        token='error'
                        lexema=cadena[indice]
                        num='x'
                    indice+=1
                elif estado==0:
                    if cadena[indice].isdigit() or cadena[indice].isalpha() or cadena[indice]=='_':
                        estado=0
                        lexema+=cadena[indice]
                        token='id'
                        indice+=1
                        num=0
                    else:
                        estado=23 
                elif estado==18:
                    if cadena[indice]=='=':
                        lexema+=cadena[indice]
                        token='opIgualdad'
                        indice+=1
                        num=11
                        estado=23
                    if cadena[indice]=='>':
                        lexema+=cadena[indice]
                        token='opRelacional'
                        indice+=1
                        num=7
                        estado=23
                    else:
                        estado=23
                elif estado==1:
                    if cadena[indice].isdigit() and decim==False:
                        estado=1
                        lexema+=cadena[indice]
                        token='entero'
                        indice+=1
                        num=1
                    elif cadena[indice].isdigit() and decim==True:
                        estado=1
                        lexema+=cadena[indice]
                        token='constante decimal'
                        indice+=1
                        num=2
                        decim=True
                    elif cadena[indice]=='.':
                        estado=1
                        lexema+=cadena[indice]
                        token='constante decimal'
                        indice+=1
                        num=2
                        decim=True
                    else:
                        estado=23
                        decim=False
                elif estado==8:
                    if cadena[indice-1]=='|'and cadena[indice]=='|':
                        lexema+=cadena[indice]
                        token='opOr'
                        estado=23
                        indice+=1   
                        num=8
                    elif cadena[indice-1]=='&'and cadena[indice]=='&':
                        lexema+=cadena[indice]
                        token='opAnd'
                        estado=23
                        indice+=1     
                        num=9
                    else:
                        estado=23
                elif estado==7:
                    if(cadena[indice-1]=='<' or cadena[indice-1]=='>') and cadena[indice]=='=':
                        lexema+=cadena[indice]
                        token='opRelacional'
                        estado=7   
                        num=7
                        indice+=1
                    elif cadena[indice-1]=='!' and cadena[indice]=='=':
                        lexema+=cadena[indice]
                        token='opIgualdad'
                        estado=7   
                        num=11
                        indice+=1
                    else:
                        estado=23
            estado=-1
            elementos.append({'token':token,'lexema':lexema, 'num':num})
    for elemento in elementos:
        if elemento['lexema']=="if":
            elemento['token']="condicional SI"
            elemento['num']=19
        if elemento['lexema']=="while":
            elemento['token']="bucle while"
            elemento['num']=20
        if elemento['lexema']=="return":
            elemento['token']="valor retornado"
            elemento['num']=21
        if elemento['lexema']=="else":
            elemento['token']="else"
            elemento['num']=22
        if elemento['lexema']=="int":
            elemento['token']="Tipo int"
            elemento['num']=4
        if elemento['lexema']=="float":
            elemento['token']="Tipo float"
            elemento['num']=4
        if elemento['lexema']=="void":
            elemento['token']="Tipo void"
            elemento['num']=4
    return elementos
ladoderecho=[1,0,2,1,1,4,0,3,6,0,3,0,4,3,0,2,1,1,0,2,4,6,5,3,2,0,2,3,0,1,0,2,0,3,1,1,1,1,1,4,1,1,3,2,2,3,3,3,3,3,3,1]
ladoizquierdo=[24,25,25,26,26,27,28,28,29,30,30,31,31,32,33,33,34,34,35,35,36,36,36,36,36,37,37,38,39,39,40,40,41,41,42,42,42,42,42,43,44,44,45,45,45,45,45,45,45,45,45,45]
liobj=["programa","Definiciones","Definiciones","Definicion","Definicion","DefVar",
       "ListaVar","ListaVar","DefFunc","Parametros","Parametros","ListaParam","ListaParam",
       "BloqFunc","DefLocales","DefLocales","DefLocal","DefLocal","Sentencias","Sentencias",
       "Sentencia","Sentencia","Sentencia","Sentencia","Sentencia","Otro","Otro","Bloque","ValorRegresa",
       "ValorRegresa","Argumentos","Argumentos","ListaArgumentos","ListaArgumentos",
       "Termino","Termino","Termino","Termino","Termino","LlamadaFunc","SentenciaBloque","SentenciaBloque",
       "Expresion","Expresion","Expresion","Expresion","Expresion","Expresion","Expresion","Expresion",
       "Expresion","Expresion"]
def getentrada():
    label.configure(text="Ingrese cadena",fg="black")
    frame.configure(state=NORMAL)
    frame.delete('1.0', END)
    frame.insert(END,"lexema")
    frame.insert(END, '\t\t')
    frame.insert(END,"token")
    frame.insert(END, '\t\t')
    frame.insert(END,"valor numerico en tabla")
    frame.insert(END, '\n\n')
    entrada = entradatk.get("1.0",'end-1c')
    cuadroporllenar.configure(state=NORMAL)
    cuadroporllenar.delete('1.0', END)
    cuadroporllenar.configure(state=DISABLED)
    if entrada == "":
        return
    elem=analizadorLexico(entrada)
    tamaño=len(elem)
    lisele=list(elem)
    for i in range(tamaño):
        frame.insert(END,lisele[i].get("lexema"))
        frame.insert(END, '\t\t')
        frame.insert(END,lisele[i].get("token"))
        frame.insert(END, '\t\t\t')
        frame.insert(END,lisele[i].get("num"))
        frame.insert(END, '\n')
    pila=[]
    pila.append("$")
    pila.append(0)
    pilaobj=[]
    pilaobj.append("$")
    pilaobj.append(0)
    cont=0
    fila=pila[-1]
    while cont < len(lisele):
        fila=pila[-1]
        columna=int(lisele[cont].get("num"))
        accion=(tabla.iloc[fila,columna])
        cuadroporllenar.configure(state=NORMAL)
        cuadroporllenar.insert(END,pilaobj)
        cuadroporllenar.insert(END,'\n')
        cuadroporllenar.configure(state=DISABLED)
        if (accion>0):
            pila.append(lisele[cont].get("num"))
            pila.append(tabla.iloc[fila,columna])
            objeto1=NoTerminal(lisele[cont].get("lexema"))
            pilaobj.append(objeto1.val())
            objeto2=Estado(tabla.iloc[fila,columna])
            pilaobj.append(objeto2.val())
            cont+=1
        elif (accion==0):
            label.configure(text="Cadena invalida",fg="red")
            break
        elif (accion==-1):
            label.configure(text="Cadena valida",fg="green")
            break
        elif(accion<-1):
            if len(pila)<1:
                break
            for i in range (ladoderecho[abs(accion)-2]*2):
                pila.pop()
                pilaobj.pop()
            fila=pila[-1]
            columna=ladoizquierdo[abs(accion)-2]
            pila.append(columna)
            pila.append(tabla.iloc[fila,columna])
            objeto3=Terminal(liobj[columna-24])
            pilaobj.append(objeto3.val())
            objeto3=Terminal(tabla.iloc[fila,columna])
            pilaobj.append(objeto3.val())
        elem.clear()
    elementos.clear()
    entrada=""
    frame.configure(state=DISABLED)
entradatk=Text(top, width=20, height=10)
entradatk.grid(column=0, row=0)
scroll=Scrollbar(top)
entradatk.configure(yscrollcommand=scroll.set)
scroll.config(command=entradatk.yview)
scroll.grid(column=1, row=0, sticky='ns')
validar=Button(top, text="Validar",command=getentrada)
validar.grid(column=3,row=0)
top.grid_columnconfigure(2, minsize=70)
top.grid_columnconfigure(4, minsize=70)
cuadroporllenar=Text(top,width=100, height=10,bg="white",state=DISABLED)
cuadroporllenar.place(x=350, y=10, height=160, width=440)
frame=Text(top,bg="white",state=DISABLED)
frame.place(x=0,y=180,height=300, width=785)
vscrollbar = Scrollbar(top, orient=VERTICAL,command=frame.yview)
vscrollbar.place(x=785,y=180,height=300)
frame.configure(yscrollcommand=vscrollbar.set)
label=Label(top,text="Ingrese cadena")
label.place(x=235,y=120)
top.mainloop()