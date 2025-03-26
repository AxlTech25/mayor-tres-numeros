"""
Determina el mayor de tres numeros ingresados por el teclado
"""
numero1=int(input("Ingresa el primer numero: "))
numero2=int(input("Ingresa el segundo numero: "))
numero3=int(input("Ingresa el tercer numero: "))

if numero1>numero2:
    temporal=numero1
    numero1=numero2
    numero2=temporal

if numero2>numero3:
    temporal=numero2
    numero2=numero3
    numero3=temporal

if numero1>numero2:
    temporal=numero1
    numero1=numero2
    numero2=temporal

print(f"numero ordenados: {numero1},{numero2},{numero3}")
print(f"El mayor es: {numero3}")
