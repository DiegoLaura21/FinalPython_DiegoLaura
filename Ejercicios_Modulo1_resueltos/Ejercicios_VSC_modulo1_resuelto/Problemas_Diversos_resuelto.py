#Problema1

inversion = float(input("Introduce cantidad de dinero depositada en la cuenta de ahorros: "))
interes = 0.04
balance1 = inversion * (1 + interes)
print("Balance tras el primer año:" + str(round(balance1, 2)))
balance2 = balance1 * (1 + interes)
print("Balance tras el segundo año:" + str(round(balance2, 2)))
balance3 = balance2 * (1 + interes)
print("Balance tras el tercer año:" + str(round(balance3, 2)))

#Problema2

from math import sqrt
A = int(input("Ingrese el coeficiente de la variable cuadrática\n"))
B = int(input("Ingrese el coeficiente de la variable lineal\n"))
C = int(input("Ingrese el término independiente\n"))
x1= 0
x2= 0
if ((B**2)-4*A*C) < 0:
  print("La solución de la ecuación es con números complejos")
else:
  x1 = (-B+sqrt(B**2-(4*A*C)))/(2*A)
  x2 = (-B-sqrt(B**2-(4*A*C)))/(2*A)
  print("Las soluciones de la ecuación son:")
  print(x1)
  print(x2)
