def es_letra(caracter):
    return 'a' <= caracter <= 'z' or 'A' <= caracter <= 'Z'

def es_digito(caracter):
    return '0' <= caracter <= '9'

def analizar_identificador(codigo, posicion):
    identificador = ''
    while posicion < len(codigo) and (es_letra(codigo[posicion]) or es_digito(codigo[posicion])):
        identificador += codigo[posicion]
        posicion += 1
    return ('Identificador', identificador), posicion

def analizar_entero(codigo, posicion):
    entero = ''
    while posicion < len(codigo) and es_digito(codigo[posicion]):
        entero += codigo[posicion]
        posicion += 1
    return ('Entero', entero), posicion

def analizar_real(codigo, posicion):
    numero = ''
    punto_encontrado = False

    while posicion < len(codigo) and (es_digito(codigo[posicion]) or codigo[posicion] == '.'):
        if codigo[posicion] == '.':
            if punto_encontrado:
                raise ValueError(f"Formato de número real inválido: {numero}")
            punto_encontrado = True
        numero += codigo[posicion]
        posicion += 1

    if punto_encontrado and len(numero.split('.')[1]) > 0:
        return ('Real', numero), posicion
    else:
        raise ValueError(f"Formato de número real inválido: {numero}")

def analizar_token(codigo, posicion):
    if codigo[posicion] == '+':
        return ('Operador adicion', '+'), posicion + 1
    elif codigo[posicion] == '-':
        return ('Operador adicion', '-'), posicion + 1
    elif codigo[posicion] == '*':
        return ('Operador multiplicacion', '*'), posicion + 1
    elif codigo[posicion] == '/':
        return ('Operador multiplicacion', '/'), posicion + 1
    elif codigo[posicion] == '=':
        if posicion + 1 < len(codigo) and codigo[posicion + 1] == '=':
            return ('Operador relacional', '=='), posicion + 2
        return ('Operador asignacion', '='), posicion + 1
    elif codigo[posicion] == '<':
        if posicion + 1 < len(codigo) and codigo[posicion + 1] == '=':
            return ('Operador relacional', '<='), posicion + 2
        return ('Operador relacional', '<'), posicion + 1
    elif codigo[posicion] == '>':
        if posicion + 1 < len(codigo) and codigo[posicion + 1] == '=':
            return ('Operador relacional', '>='), posicion + 2
        return ('Operador relacional', '>'), posicion + 1
    elif codigo[posicion] == '!':
        if posicion + 1 < len(codigo) and codigo[posicion + 1] == '=':
            return ('Operador relacional', '!='), posicion + 2
        return ('Operador logico', '!'), posicion + 1
    elif codigo[posicion] == '&':
        if posicion + 1 < len(codigo) and codigo[posicion + 1] == '&':
            return ('Operador logico', '&&'), posicion + 2
        else:
            raise ValueError(f"Caracter inesperado: {codigo[posicion]}")
    elif codigo[posicion] == '|':
        if posicion + 1 < len(codigo) and codigo[posicion + 1] == '|':
            return ('Operador logico', '||'), posicion + 2
        else:
            raise ValueError(f"Caracter inesperado: {codigo[posicion]}")
    elif codigo[posicion] == '(':
        return ('Parentesis', '('), posicion + 1
    elif codigo[posicion] == ')':
        return ('Parentesis', ')'), posicion + 1
    elif codigo[posicion] == '{':
        return ('Llave', '{'), posicion + 1
    elif codigo[posicion] == '}':
        return ('Llave', '}'), posicion + 1
    elif codigo[posicion] == ';':
        return ('Punto y coma', ';'), posicion + 1
    else:
        raise ValueError(f"Caracter inesperado: {codigo[posicion]}")

def analizar(codigo):
    posicion = 0
    tokens = []

    while posicion < len(codigo):
        if codigo[posicion].isspace():
            posicion += 1
        elif es_letra(codigo[posicion]):
            token, posicion = analizar_identificador(codigo, posicion)
            tokens.append(token)
        elif es_digito(codigo[posicion]):
            if posicion + 1 < len(codigo) and codigo[posicion + 1] == '.':
                token, posicion = analizar_real(codigo, posicion)
            else:
                token, posicion = analizar_entero(codigo, posicion)
            tokens.append(token)
        else:
            token, posicion = analizar_token(codigo, posicion)
            tokens.append(token)

    return tokens

# Ejemplo de uso
codigo_fuente = "(var1 = 123 + - { x && y || !z } );"
tokens = analizar(codigo_fuente)

for token in tokens:
    print(token)
