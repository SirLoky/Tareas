#Ejercicio 1

"""def calcular_factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * calcular_factorial(n-1)
numero = int(input("Por favor, ingresa un número entero: "))

factorial = calcular_factorial(numero)
print("El factorial de", numero, "es:", factorial)
"""
#Ejercicio 2

"""def calcular_suma(n):
    if n == 0:
        return 0
    else:
        return n + calcular_suma(n-1)

# Ejemplo de uso de la función
numero = int(input("Por favor, ingresa un número entero: "))

suma = calcular_suma(numero)
print("La suma de los primeros", numero, "números naturales es:", suma)
"""

#Ejercicio 3

"""def calcular_fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return calcular_fibonacci(n-1) + calcular_fibonacci(n-2)

# Ejemplo de uso de la función
numero = int(input("Por favor, ingresa un número entero: "))

fibonacci = calcular_fibonacci(numero)
print("El", numero, "número de la secuencia de Fibonacci es:", fibonacci)
"""

#Ejercicio 4

"""def calcular_potencia(x, n):
    if n == 0:
        return 1
    else:
        return x * calcular_potencia(x, n-1)

# Ejemplo de uso de la función
base = int(input("Por favor, ingresa la base: "))
exponente = int(input("Por favor, ingresa el exponente: "))

potencia = calcular_potencia(base, exponente)
print(base, "elevado a la potencia", exponente, "es:", potencia)
"""

#Ejercicio 5

"""def calcular_suma_digitos(numero):
    if numero < 10:
        return numero
    else:
        ultimo_digito = numero % 10
        return ultimo_digito + calcular_suma_digitos(numero // 10)

# Ejemplo de uso de la función
numero = int(input("Por favor, ingresa un número entero positivo: "))

suma_digitos = calcular_suma_digitos(numero)
print("La suma de los dígitos de", numero, "es:", suma_digitos)
"""

#Ejercicio 6

"""def contar_caracter(cadena, caracter):
    if len(cadena) == 0:
        return 0
    else:
        if cadena[0] == caracter:
            return 1 + contar_caracter(cadena[1:], caracter)
        else:
            return contar_caracter(cadena[1:], caracter)

# Ejemplo de uso de la función
cadena = input("Por favor, ingresa una cadena de texto: ")
caracter = input("Por favor, ingresa un carácter: ")

cantidad = contar_caracter(cadena, caracter)
print("El carácter", caracter, "aparece", cantidad, "veces en la cadena.")
"""

#Ejercicio 7

"""def calcular_suma_lista(lista):
    if len(lista) == 0:
        return 0
    else:
        return lista[0] + calcular_suma_lista(lista[1:])

# Ejemplo de uso de la función
lista = [1, 2, 3, 4, 5]

suma = calcular_suma_lista(lista)
print("La suma de los elementos en la lista es:", suma)
"""

