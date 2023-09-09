"""Ejercicio#1"""

"""nombre = input("Por favor, ingresa tu nombre: ")
print("Hola, " + nombre + "Bienvenido")"""

"""Ejercicio#2"""

"""n = int(input("Por favor, ingresa un número entero: "))
suma = 0
for i in range(1, n+1):
    suma += i
print("La suma de todos los números del 1 al " + str(n) + " es " + str(suma))"""

"""Ejercicio#3"""

"""print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")

opcion = int(input("Elige una opción (1, 2, 3, 4): "))

num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))

if opcion == 1:
    resultado = num1 + num2
    print("El resultado es: ", resultado)
elif opcion == 2:
    resultado = num1 - num2
    print("El resultado es: ", resultado)
elif opcion == 3:
    resultado = num1 * num2
    print("El resultado es: ", resultado)
elif opcion == 4:
    if num2 != 0:
        resultado = num1 / num2
        print("El resultado es: ", resultado)
    else:
        print("Error: División por cero no está permitida.")
else:
    print("Opción no válida.")
"""

"""Ejercicio#4"""

"""n = int(input("Por favor, ingresa un número: "))
for i in range(1, 11):
    print(n, "x", i, "=", n*i)
"""

"""Ejercicio#5"""

"""lista = list(map(int, input("Por favor, ingresa una lista de números, separados por espacios: ").split()))
objetivo = int(input("Por favor, ingresa un número objetivo: "))

if objetivo in lista:
    print("El número objetivo está en la lista.")
else:
    print("El número objetivo no está en la lista.")"""
    
"""Ejercicio#6"""

"""n = int(input("Por favor, ingresa un número: "))
if n % 2 == 0:
    print("El número es par.")
else:
    print("El número es impar.")"""
    
"""Ejercicio#7"""

"""lista = list(map(int, input("Por favor, ingresa una lista de números, separados por espacios: ").split()))
maximo = max(lista)
print("El número máximo es:", maximo)
"""

"""Ejercicio#8"""

"""def calcular_potencia(x, n):
    resultado = x ** n
    return resultado

# Ejemplo de uso de la función
base = float(input("Por favor, ingresa la base: "))
exponente = int(input("Por favor, ingresa el exponente: "))

potencia = calcular_potencia(base, exponente)
print("El resultado de", base, "elevado a la potencia", exponente, "es:", potencia)
"""

"""Ejercicio#9"""

"""cadena = input("Por favor, ingresa una cadena: ")
vocales = "aeiouAEIOU"
contador = 0

for caracter in cadena:
    if caracter in vocales:
        contador += 1

print("La cantidad de vocales en la cadena es:", contador)
"""

"""Ejercicio#10"""

"""n = int(input("Por favor, ingresa un número: "))

for i in range(1, n+1):
    print('*' * i)
"""