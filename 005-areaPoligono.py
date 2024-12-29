# 
#  * Crea una única función (importante que sólo sea una) que sea capaz
#  * de calcular y retornar el área de un polígono.
#  * - La función recibirá por parámetro sólo UN polígono a la vez.
#  * - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
#  * - Imprime el cálculo del área de un polígono de cada tipo.
#  

def calcular_area(cantidad_lados, base, altura):
    if cantidad_lados == 3:
        area = (base * altura) / 2
    elif cantidad_lados == 4:
        area = (base * altura)
    else:
        return "Solamente se puede calcular el área de un poligono de 3 o 4 lados."
    return area

resultado = calcular_area(3, 5, 3)

print(f"El área es: {resultado}")