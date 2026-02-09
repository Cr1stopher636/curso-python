###
# exercises.py
# Ejercicios para practicar los conceptos aprendidos en las lecciones.
###

from os import system
if system("clear") != 0: system("cls")

print("\nEjercicio 1: Imprimir mensajes")
print("Escribe un programa que imprima tu nombre y tu ciudad en líneas separadas.")


### Completa aquí

print("Nombre: Ricardo")
print("Ciudad: CDMX")

print("\nEjercicio 2: Muestra los tipos de datos de las siguientes variables:")
print("Usa el comando 'type()' para determinar el tipo de datos de cada variable.")
a = 15
b = 3.14159
c = "Hola mundo"
d = True
e = None

### Completa aquí

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))

print("\nEjercicio 3: Casting de tipos")
print("Convierte la cadena \"12345\" a un entero y luego a un float.")
print("Convierte el float 3.99 a un entero. ¿Qué ocurre?")

### Completa aquí

cadena_entero = int("12345")
cadena_decimal = float("12345")
decimal_float = float(int("12345"))


print(type(cadena_entero))
print(type(cadena_decimal))
print(type(decimal_float))


print("\nEjercicio 4: Variables")
print("Crea variables para tu nombre, edad y altura.")
print("Usa f-strings para imprimir una presentación.")


# "Hola! Me llamo midudev y tengo 39 años, mido 1.70 metros"

### Completa aquí

nombre = "ricardo"
edad = 22
altura = 1.93

print(f"Hola {nombre}, tienes {edad} años, y mides {altura} m")

print("\nEjercicio 5: Números")
print("1. Crea una variable con el número PI (sin asignar una variable)")
print("2. Redondea el número con round()")
print("3. Haz la división entera entre el número que te salió y el número 2")
print("4. El resultado debería ser 1")

resultado = round(3.1416) // 2
print(resultado)

