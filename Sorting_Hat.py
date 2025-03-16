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

if Question_2 ==1:
    Hufflepuff =+2
elif Question_2 ==2:
    Slytherin =+2
elif Question_2 ==3:
    Ravenclaw=+2
elif Question_2 ==4:
    Gryffindor=+2
else:
    print("Tu respuesta es incorrecta")

print("3)¿Que instrumento te gusta más escuchar?")
Question_3=int(input("1-Violin, 2-Trompeta, 3-Piano, 4-Bateria (introduce 1-4)"))

if Question_3 ==1:
    Slytherin =+4
elif Question_3 == 2:
    Hufflepuff =+4
elif Question_3 ==3:
    Ravenclaw= +4
elif Question_3 ==4:
    Gryffindor= +4
else:
    print("Tu respuesta es incorrecta")

print("Gryffindor: ", Gryffindor)
print("Ravenclaw: ", Ravenclaw)
print("Hufflepuff: ", Hufflepuff)
print("Slytherin: ", Slytherin)

most_points = max(Gryffindor, Ravenclaw, Hufflepuff, Slytherin)

if Gryffindor == most_points:
  print('🦁 Gryffindor!')
elif Ravenclaw == most_points:
  print('🦅 Ravenclaw!')
elif Hufflepuff == most_points:
  print('🦡 Hufflepuff!')
else:
  print('🐍 Slytherin!')