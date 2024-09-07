nota1 = float(input("Ingrese su primera calificacion: "))
nota2 = float(input("Ingrese su segunda calificacion: "))
nota3 = float(input("Ingrese su tercera calificacion: "))
nota4 = float(input("Ingrese su cuarta calificacion: "))
matricula = float(input("Ingrese el costo de la matricula: "))

promedio = (nota1+nota2+nota3+nota4)/4

if 4 <= promedio <= 5:
    costo_matricula = matricula * 0.8
    print(f"Estudiante su rendimiento se clasifica en excelente por lo tanto tiene un descuento y el valor de la matricula es: {costo_matricula}")
elif 3 <= promedio <= 3.99:
    costo_matricula =matricula
    print(f"Estudiante su rendimiento se clasifica en bueno  y el valor de la matricula es: {matricula}")
elif 0 <= promedio <= 2.99:
    costo_matricula = matricula
    print(f"Estudiante su rendimiento se clasifica en deficiente  y el valor de la matricula es: {matricula}")
else:
    print("Valor invalido")


