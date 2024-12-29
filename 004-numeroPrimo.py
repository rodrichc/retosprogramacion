# 
#  * Escribe un programa que se encargue de comprobar si un número es o no primo.
#  * Hecho esto, imprime los números primos entre 1 y 100.
#  

def verificar_numero_primo(numero):
    if numero == 1:
        return False
    for num in range(2, numero):
        if numero % num == 0:
            return False
    return True
    
for num in range(1, 101):
    resultado = verificar_numero_primo(num)
    if resultado:
        print (num)