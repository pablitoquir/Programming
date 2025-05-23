print("Bienvenido a la calculadora básica")
print("Seleccione una operación:")
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")

opcion = input("Ingrese el número de la opción: ")

numero1 = float(input("Ingrese el primer número: "))
numero2 = float(input("Ingrese el segundo número: "))

if opcion == "1":
    resultado = numero1 + numero2
    print("La suma es:", resultado)
elif opcion == "2":
    resultado = numero1 - numero2
    print("La resta es:", resultado)
elif opcion == "3":
    resultado = numero1 * numero2
    print("La multiplicación es:", resultado)
elif opcion == "4":
    if numero2 != 0:
        resultado = numero1 / numero2
        print("La división es:", resultado)
    else:
        print("Error: no se puede dividir por cero.")
else:
    print("Opción inválida.")
