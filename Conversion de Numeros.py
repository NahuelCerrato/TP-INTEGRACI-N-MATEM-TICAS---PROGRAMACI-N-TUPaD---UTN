# EJEMPLO_2: Conversión de Números
# Este programa convierte números entre decimal y binario (en ambas direcciones).
# Incluye validación de entrada para evitar errores por datos incorrectos.

# Importamos la librería math para usar trunc() más adelante
import math

# Mensaje de bienvenida e instrucciones para el usuario
print ("Conversión de Números - Sistema Binario/Decimal")
print("")
print ("Seleccione una opcion segun la conversion que necesite realizar: ")
print("")
print ("1: Decimal a Binario")
print("")
print ("2: Binario a Decimal")

# Inicializamos una variable booleana para validar la entrada del usuario
es_valido = False
while not es_valido:
    entrada = input("Ingrese 1 o 2: ")
    if entrada.isnumeric():  # Verifica si la entrada es numérica
        conversion = int(entrada)
        if conversion == 1 or conversion == 2:  # Verifica que sea 1 o 2
            es_valido = True
        else:
            print("¡Solo puede ingresar 1 o 2!")
    else:
        print("¡Debe ingresar un número!")

# Doble validación extra por si acaso
while conversion != 1 and conversion != 2:
    print ("Ingrese una opcion valida! 1 o 2: ")
    conversion = int(input())

# ----- CONVERSIÓN DE DECIMAL A BINARIO -----
if conversion == 1:
    es_valido = False
    while not es_valido:
        entrada = input("Ingrese el numero Decimal a convertir en Binario: ")
        if entrada.isnumeric():  # Asegura que el número sea un entero positivo
            es_valido = True
        else:
            print("¡Debe ingresar un número entero positivo!")

    # Se convierte la entrada a entero
    numero = int(entrada)
    acumulador_restos = ""  # Almacena los restos de la división por 2
    while numero != 0:
        resto = numero % 2  # Calcula el resto (0 o 1)
        acumulador_restos += str(resto)  # Lo agrega como texto
        numero = numero // 2  # División entera por 2

    # Función que invierte una cadena (ya que los restos se obtienen en orden inverso)
    def invertirCadena(cadena):
        invertida = ""
        for caracter in cadena:
            invertida = caracter + invertida
        return invertida

    # Muestra el número en binario
    print(f"El numero en sistema Binario es: {invertirCadena(acumulador_restos)}")

# ----- CONVERSIÓN DE BINARIO A DECIMAL -----
else:
    acumulador = 0  # Acumula el resultado en decimal

    # Validación para asegurar que el número ingresado es binario (solo contiene 0 y 1)
    es_binario = False
    while not es_binario:
        numero = input("Ingrese el numero Binario a convertir en Decimal: ")
        es_binario = all(caracter in '01' for caracter in numero)  # Verifica cada carácter
        if not es_binario:
            print("El numero no es Binario!")

    # Conversión manual de binario a decimal
    numero = int(numero)  # Convertimos el string a entero
    digitos = len(str(numero))  # Cantidad de cifras
    for c in range(digitos):
        ultimo_digito = numero % 10  # Tomamos el último dígito
        a_sumar = ultimo_digito * (2 ** c)  # Aplicamos la fórmula binaria
        acumulador += a_sumar
        numero = math.trunc(numero / 10)  # Eliminamos el dígito ya procesado

    # Muestra el número en decimal
    print(f"El numero en sistema Decimal es: {acumulador}")
