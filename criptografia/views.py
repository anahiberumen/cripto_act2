from django.shortcuts import render
import codecs
# Create your views here.
def proceso(request):
    if request.method == 'POST':
        resultado =""
        mensaje = (request.POST.get("mensaje")).lower()
        llave = request.POST.get("llave")
        opcion = request.POST.get("opcion")
        metodo = request.POST.get("metodo")
#------------------------------------------------------------------
        if metodo == "1":
            if opcion == "cifrar":
                resultado = polybios_cifrar(mensaje)
            else:
                resultado = polybios_descifrar(mensaje)
#------------------------------------------------------------------
        elif metodo == "2":
            if opcion == "cifrar":
                resultado = cesar_cifrar(mensaje)
            else:
                resultado = cesar_descifrar(mensaje)

#------------------------------------------------------------------
        elif metodo == "3":
            if opcion == "cifrar":
                resultado = alberti_cifrar(mensaje, llave)
            else:
                resultado = alberti_descifrar(mensaje, llave)
#-------------------------------------------------------------------

        elif metodo == "4":
            if opcion == "cifrar":
                resultado = vigenere_cifrar(mensaje, llave)
            else:
                resultado = vigenere_descifrar(mensaje, llave)


        elif metodo == "5":
            if opcion == "cifrar":
                resultado = playfair_cifrar(mensaje)
            else:
                resultado = playfair_descifrar(mensaje)


        elif metodo == "6":
            if opcion == "cifrar":
                resultado = hill_cifrar(mensaje)
            else:
                resultado = hill_descifrar(mensaje)
        
        return render(request, 'resultado.html', {'res': resultado})

    return render(request, 'process.html')
#----------------------------------POLYBIOS-----------------------------------------------
def polybios_cifrar(mensaje):
    resultado = ""
    for c in mensaje:
        if ord(c) <= 122 and ord(c) >= 97:
            fila = int((ord(c) - 97)/5) 
            columna = ((ord(c) - 97) % 5)

            if c == 'k':
                fila = fila - 1
                columna = 4 - columna

            elif ord(c) >= ord('j'):
                if columna == 0:
                    columna = 5
                    fila = fila - 1
                columna = columna - 1
            
            resultado = resultado + chr(fila + 97) + chr(columna + 97)

        elif ord(c) == 32:
            resultado = resultado + " "
    return resultado

def polybios_descifrar(mensaje):
    resultado = ""
    i = 0
    while i < int(len(mensaje)-1):
        a = ord(mensaje[i]) - 97
        b = ord(mensaje[i+1]) - 97
        if a == 1 and b == 3:
            resultado = resultado + "[i/j]"
            i = i+1
        elif (a <= 4 and a >= 0) and (b <= 4 and b >= 0):
            pos = (a*5) + b

            if (a == 1 and b >= 3) or (a > 1):
                pos = pos + 1
            print(pos)
            resultado = resultado + chr(pos + 97)
            i = i+1
        elif ord(mensaje[i]) == 32:
            resultado = resultado + " "
        i = i+1
    return resultado
#------------------------------------CESAR------------------------------------------------
def cesar_cifrar(mensaje):

    resultado = ""
    for c in mensaje:
        if ord(c) <= 122 and ord(c) >= 97:
            numero = ord(c) - 100
            numero = (numero % 26) + 97
            letra = chr(numero)
            resultado = resultado + letra
        elif ord(c) == 32:
            resultado = resultado + " "
    return resultado
    

def cesar_descifrar(mensaje):
    resultado = ""
    for c in mensaje:
        if ord(c) <= 122 and ord(c) >= 97:
            numero = ord(c) - 94
            numero = (numero % 26) + 97
            letra = chr(numero)
            resultado = resultado + letra
        elif ord(c) == 32:
            resultado = resultado + " "
    return resultado
#------------------------------------------------------------------------
def alberti_cifrar(mensaje, llave):
    resultado = ""
    if len(llave) == 2:
        diff = abs((ord(llave[0]) - 97) - (ord(llave[1]) - 97))
        print(diff)
        for c in mensaje:
            if ord(c) <= 122 and ord(c) >= 97:
                numero = ord(c) - 97
                numero = numero + diff
                numero = (numero % 26) + 97
                letra = chr(numero)
                resultado = resultado + letra
            elif ord(c) == 32:
                resultado = resultado + " "
    else:
        return "La llave debe de contener 2 letras alfabeticas"
    return resultado

def alberti_descifrar(mensaje, llave):
    resultado = ""
    if len(llave) == 2:
        diff = abs((ord(llave[0]) - 97) - (ord(llave[1]) - 97))
        print(diff)
        for c in mensaje:
            if ord(c) <= 122 and ord(c) >= 97:
                numero = ord(c) - 97
                numero = numero - diff
                numero = (numero % 26) + 97
                letra = chr(numero)
                resultado = resultado + letra
            elif ord(c) == 32:
                resultado = resultado + " "
    else:
        return "La llave debe de contener 2 letras alfabeticas"
    return resultado

def vigenere_cifrar(mensaje, llave):
    return "kk4"

def vigenere_descifrar(mensaje, llave):
    return "kk4"

def playfair_cifrar(mensaje):
    return "kk5"

def playfair_descifrar(mensaje):
    return "kk5"

def hill_cifrar(mensaje):
    return "kk6"

def hill_descifrar(mensaje):
    return "kk6"
