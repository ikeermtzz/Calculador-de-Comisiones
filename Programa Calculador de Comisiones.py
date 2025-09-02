#Trabajo en empresa donde reciben un 13% de comisiones por cada venta, entonces tu jefe quiere que crees un programa para ayudarles a calcular las comisiones mediante su nombre y cuantas ventas hicieron

nombre = input("¿Cuál es tu nombre? ")
ventas = int(input("¿Cuántas ventas totales tuviste este mes? (Dinero) "))
comision = round((ventas*13)/100,2)
print (f"{nombre} tu comisión generada este mes es de ${comision} pesos" )