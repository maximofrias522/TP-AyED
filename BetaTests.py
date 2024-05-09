try:
    numero = int(input("Ingrese un número: "))
    resultado = 10 / numero
    print("El resultado es:", resultado)
except ZeroDivisionError:
    print("No se puede dividir por cero.")
except ValueError:
    print("Debe ingresar un número válido.")
