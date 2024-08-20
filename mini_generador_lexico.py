def es_letra(caracter):
    return 'a' <= caracter <= 'z' or 'A' <= caracter <= 'Z'

def es_digito(caracter):
    return '0' <= caracter <= '9'

def analizar_identificador(codigo, posicion):
    identificador = ''
    while posicion < len(codigo) and (es_letra(codigo[posicion]) or es_digito(codigo[posicion])):
        identificador += codigo[posicion]
        posicion += 1
    return identificador, posicion

def analizar_real(codigo, posicion):
    numero = ''
    punto_encontrado = False

    # Analiza la parte entera
    while posicion < len(codigo) and es_digito(codigo[posicion]):
        numero += codigo[posicion]
        posicion += 1

    # Verifica si hay un punto decimal
    if posicion < len(codigo) and codigo[posicion] == '.':
        punto_encontrado = True
        numero += '.'
        posicion += 1

        # Analiza la parte fraccionaria
        while posicion < len(codigo) and es_digito(codigo[posicion]):
            numero += codigo[posicion]
            posicion += 1

    if punto_encontrado and len(numero.split('.')[1]) > 0:
        return numero, posicion
    else:
        raise ValueError(f"Formato de número real inválido: {numero}")

def analizar(codigo):
    posicion = 0
    tokens = []

    while posicion < len(codigo):
        if codigo[posicion].isspace():
            posicion += 1
        elif es_letra(codigo[posicion]):
            identificador, posicion = analizar_identificador(codigo, posicion)
            tokens.append(('Identificador', identificador))
        elif es_digito(codigo[posicion]):
            real, posicion = analizar_real(codigo, posicion)
            tokens.append(('Real', real))
        else:
            print(f"Caracter inesperado: {codigo[posicion]}")

    return tokens

# Ejemplo de uso
codigo_fuente = "var1 123.45 var2 67.89 var3"
tokens = analizar(codigo_fuente)

for token in tokens:
    print(token)
