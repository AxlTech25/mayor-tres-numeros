"""
Determina el mayor de tres numeros ingresados por el teclado
"""
def intercambiar_valores(numero1,numero2):
    temporal = numero1
    numero1 = numero2
    numero2 = temporal
    return numero1,numero2
numero1=int(input("Ingresa el primer numero: "))
numero2=int(input("Ingresa el segundo numero: "))
numero3=int(input("Ingresa el tercer numero: "))

if numero1>numero2:
    numero1,numero2 =  intercambiar_valores(numero1,numero2)

if numero2>numero3:
    numero2, numero3 = intercambiar_valores(numero2,numero3)

if numero1>numero2:
    numero1,numero2 =  intercambiar_valores(numero1,numero2)

print(f"numero ordenados: {numero1},{numero2},{numero3}")
print(f"El mayor es: {numero3}")
