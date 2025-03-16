Gryffindor= 0
Hufflepuff=0
Slytherin=0
Ravenclaw=0
print("1)Te gusta mas el amanecer o el anochecer?")
Question_1=int(input("Introduce tu respuesta(1-2)"))
if Question_1 == 1:
    Gryffindor=+1,
    Ravenclaw =+1
elif Question_1 == 2:
    Hufflepuff=+1
    Slytherin=+1
else:
    print("Tu respuesta es incorrecta")

print("2)En mi funeral, la gente me recordara como:")

Question_2= int(input("1-El Bueno, 2-El grande, 3-El sabio, 4-El audaz (tu respuesta 1-4)"))

if Question_2 == 1:
    Hufflepuff =+2
if Question_2 == 2:
    Slytherin =+2
if Question_2 == 3:
    Ravenclaw=+2
if Question_2 ==4:
    Gryffindor=+2
else:
    print("Tu respuesta es incorrecta")

    print(Gryffindor,Hufflepuff,Ravenclaw,Slytherin)