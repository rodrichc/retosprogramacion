# 
#  * Escribe una función que reciba dos palabras (String) y retorne
#  * verdadero o falso (Bool) según sean o no anagramas.
#  * - Un Anagrama consiste en formar una palabra reordenando TODAS
#  *   las letras de otra palabra inicial.
#  * - NO hace falta comprobar que ambas palabras existan.
#  * - Dos palabras exactamente iguales no son anagrama.
# 

def comprobar_anagrama(palabra1, palabra2):
    for letra in palabra1:
        if letra not in palabra2:
            return False
        elif len(palabra1) == len(palabra2):
            return True
        else:
            return False

#Prueba
resultado = comprobar_anagrama("manto", "toman")
print(resultado)