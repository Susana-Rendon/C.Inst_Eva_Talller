peso = float(input(" Ingrese su peso en kilogramos: "))
altura = float(input( " Ingrese su altura en metros: "))

imc = peso / (altura*altura)
resultado_imc = imc * 10000
#se multiplica * 10000 para conversion de unidades y asi mostar el valor de imc

print(f" Su indice de masa corporal es {resultado_imc}")
