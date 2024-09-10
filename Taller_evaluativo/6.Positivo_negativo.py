#	Verifica si 'x' es negativo, 'y' es positivo, y 'z' es cero:

x, y, z = -3, 5, 0

if x < 0:
    print(f" El numero {x} es negativo")
else:
    print(f" {x} es numero positivo")

if y > 0:
    print(f" El numero {y} es positivo")
else:
    print(f" {y} es un numero negativo")

if z == 0:
    print(f" {z} es cero")
else:
    print(f" {z} no es cero")

resultado =  (x < 0) and (y > 0) and (z == 0)
print(resultado)