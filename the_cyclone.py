#heigh =  137
#coin = 10


heigh= int(input("Introduce tu altura"))

coin= int(input("¿Cuantas monedas tienes?"))

if heigh > 137 and coin > 10:
    print("¡Disfruta del viaje!")

if heigh < 137 and coin > 10:
    print("No tienes la altura suficiente")

if heigh >137 and coin < 10:
    print("No tienes suficientes monedas")

if heigh < 137 and coin  < 10:
    print("No cumples los requisitos para entrar")


