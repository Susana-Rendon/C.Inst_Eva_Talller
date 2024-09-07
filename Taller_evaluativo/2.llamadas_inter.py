def costo_llamada(destino, duracion):

    match destino:
        case "EEUU":
            costo = 900
        case "Canada":
            costo = 800
        case "Europa":
            costo = 950
        case "Resto del mundo":
            costo = 1250
        case _:
            return "Destino inválido"

    costo_inicial = costo * duracion

    if duracion > 15:
        valor_llamada = costo_inicial * 0.8  # 20% de descuento
    else:
        valor_llamada = costo_inicial

    return f"El costo total de la llamada es: ${valor_llamada:.2f}"

destino = input("Ingrese el destino a llamar (EEUU, Canada, Europa, Resto del mundo): ")
duracion = float(input("Ingrese la duración de la llamada en minutos: "))

print(costo_llamada(destino, duracion))