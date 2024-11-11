#en un curso de computación, que consta de 24 alumnos, deberán armar un
# algoritmo que informe por pantalla el apellido y nombre junto a la nota de
# examen de cada alumno.


i = 0
while i < 24:
    apellido = input("Ingrese el apellido del alumno: ")
    nombre = input("Ingrese el nombre del alumno: ")
    nota = float(input("Ingrese la nota del examen: "))
    print(f"{apellido} {nombre} - Nota: {nota}")
    i += 1
