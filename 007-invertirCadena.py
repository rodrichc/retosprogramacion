# 
#  * Crea un programa que invierta el orden de una cadena de texto
#  * sin usar funciones propias del lenguaje que lo hagan de forma automática.
#  * - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
#  

def invertir_cadena(cadena):
    nueva_cadena = ""
    for letra in cadena[::-1]:
        nueva_cadena += letra
    print(nueva_cadena)

invertir_cadena("Estoy invertiendo esta cadena de texto.")