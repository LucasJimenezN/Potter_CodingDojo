"""
Definición del problema:
- Cada libro cuesta 8€
- Si se compran 2 libros distintos se obtiene un descuento del 5%
- Si se compran 3 libros distintos se obtiene un descuento del 10%
- Si se compran 4 libros distintos se obtiene un descuento del 20%
- Si se compran 5 libros distintos se obtiene un descuento del 25%
Hay que tener en cuenta que se puede obtener más descuento por 2 de 20% que 1 de 25% y otro de 10%.
"""

DESCUENTOS = [0.95, 0.90, 0.80, 0.75]


def price(array):
    money = 0
    dic = check_different_books(array)
    discount = check_simple_discount(dic)
    for i in array:
        money = money + 8

    if discount >= 0:
        money = money * DESCUENTOS[discount]
    return money


def check_different_books(array):
    aux = {}
    for i in array:
        if i not in aux:
            aux[i] = 1
        else:
            aux[i] += 1

    return aux


def check_simple_discount(dic):
    max_discount = -2
    for i in dic:
        max_discount += 1
    return max_discount


value = check_different_books([1, 2, 3, 4, 5, 5, 5, 4])
for i in value:
    print(f"Libro {i} hay: {value[i]} copias.")
