#•	Verifica si 'x' está entre 'y' y 'z', y si 'w' es par:
x, y, z, w = 15, 10, 20, 8

# Si x esta entre y y z
if y < x < z:
    print(f" {x}  esta entre {y} y {z}")
else:
    print(f" {x} no esta entre {y} y {z}")

# si w es par
if w % 2 == 0:
    print(f" {w} es un numero par")
else:
    print(f"{w} no es un numero par")

resultado = (y < x < z) and (w % 2 == 0)
print(resultado)
