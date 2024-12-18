## Calculadora de índice de masa corporal

# Pregunta al usuario cuánto pesa en KG y guarda el valor en una variable
peso_user = (input("Cuanto pesas en (Kg)"))  # Solicita el peso del usuario como entrada
peso_user_n = peso_user.strip().replace(",", ".")  # Elimina espacios y reemplaza comas por puntos para evitar errores
peso_user_float = float(peso_user_n)  # Convierte la cadena modificada a un número de tipo flotante

# Pregunta al usuario cuánto mide y guarda el valor en una variable
altura_user = (input("Cuanto mides en (M)"))  # Solicita la altura del usuario como entrada
altura_user_n = altura_user.strip().replace(",", ".")  # Elimina espacios y reemplaza comas por puntos
altura_user_float = float(altura_user_n)  # Convierte la cadena modificada a un número de tipo flotante

# Calcula el índice de masa corporal
imc = peso_user_float / (altura_user_float * 2)  # **ERROR**: Aquí debería ser (altura_user_float ** 2) para elevar al cuadrado
imc = round(imc, 2)  # Redondea el resultado del IMC a 2 decimales

# Imprime el encabezado del resultado
print("\n")
print("***** Este es tu índice de masa corporal *****")
print("** " + peso_user_n + " Kg" + "                                    **")  # Muestra el peso ingresado
print("** " + altura_user_n + " M" + "                                    **")  # Muestra la altura ingresada

# Evalúa el IMC y muestra la categoría correspondiente
if 0 <= imc <= 15:  # Si el IMC está entre 0 y 15
    print(f"** Estas en un peso muy bajo {imc}          **")
elif 16 < imc <= 25:  # Si el IMC está entre 16 y 25
    print(f"** Estas en un peso normal {imc}            **")
elif 26 < imc <= 33:  # Si el IMC está entre 26 y 33
    print(f"** Estas en sobrepeso {imc}                 **")
elif imc < 34:  # **ERROR**: Esta condición se ejecutará siempre que no se cumplan las anteriores
    print(f"** Tienes obesidad mórbida {imc}           **")
else:  # Si el IMC es menor a 0 (caso imposible) se imprime un error
    print("Error el número está por debajo de 0")

# Imprime el pie del resultado
print("**********************************************")