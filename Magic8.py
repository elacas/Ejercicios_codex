import random

question = input("Escribe tu pregunta:")

random_number = random.randint(1,9)

if random_number == 1:
    print("Si, definitivamente")
if random_number == 2:
    print("Asi es, sin duda")
if random_number == 3:
    print("Indudablemente")
elif random_number ==4:
    print("Respuesta confusa, inténtalo de nuevo")
if random_number ==5:
    print("Pregunta de nuevo mas tarde")
elif random_number == 6:
    print("Será mejor que no te lo diga ahora")
if random_number == 7:
    print("Mis fuentes dicen que no")
if random_number == 8:
    print("Perspectiva no tan buena")
if random_number == 9:
    print("Lo dudo")
