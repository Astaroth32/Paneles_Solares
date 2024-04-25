

print('Ingrese dimensiones del techo')

print('Ancho:')
x = int(input())
print('Largo:')
y = int(input())

print('Ingrese dimensiones del panel solar')
print('Ancho:')
a = int(input())
print('Largo:')
b = int(input())

def max_rectangles(a, b, x, y):

    # veces que cabe el ancho del panel en el ancho del techo
    count_a_x = x // a
    # veces que cabe el largo del panel en el largo del techo
    count_b_y = y // b
    # Veces que cabe el largo del panel en el ancho del techo.
    count_b_x = x // b
    # Veces que cabe el ancho del panel en el largo del techo.
    count_a_y = y // a
    
    return max(count_a_x * count_b_y, count_b_x * count_a_y)

print("Cantidad máxima de paneles solares de dimension", a, "x", b, "que caben en un techo de dimensiones", x, "x", y, ":", max_rectangles(a, b, x, y))