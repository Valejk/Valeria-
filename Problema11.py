#Ingresar un valor por teclado y determinar si es menor que 10 si está comprendido
# entre 10 y 100 o si es mayor a 100, imprimir una leyenda, repetir el proceso 10 veces.


i = 0
while i < 10:
    valor = float(input("Ingrese un valor: "))
    if valor < 10:
        print("El valor es menor que 10")
    elif 10 <= valor <= 100:
        print("El valor está entre 10 y 100")
    else:
        print("El valor es mayor a 100")
    i += 1
