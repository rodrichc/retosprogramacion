# 
#  * Escribe un programa que imprima los 50 primeros números de la sucesión
#  * de Fibonacci empezando en 0.
#  * - La serie Fibonacci se compone por una sucesión de números en
#  *   la que el siguiente siempre es la suma de los dos anteriores.
#  *   0, 1, 1, 2, 3, 5, 8, 13...
#  

def fibonacci(cantidad_resultados):
    sucesion = [0,1]
    while len(sucesion) < cantidad_resultados:
        numero = sucesion[-1] + sucesion [-2]
        sucesion.append(numero)
    return sucesion

resultado = fibonacci(50)
print(resultado)