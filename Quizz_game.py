print('Welcome to my quizz game ')
playing = input('Do you want to play this game? ')

if playing.lower() != "yes":
    quit()

print("Okay, lets play")
score = 0

q1 = input("What is the main source of light on earth? ")
if q1.lower() == "sun":
    print("Correct!" )
    score +=1
else:
    print("Incorrect")

q2 = input("What light source gives light at night on the sky? ")
if q2.lower() == "moon":
    print("Correct!" )
    score +=1
else:
    print("Incorrect")

q3 = input("What water body covers every continent? ")
if q3.lower() == "ocean":
    print("Correct!" )
    score +=1
else:
    print("Incorrect")
    
print("You got " +   str(score)  + " questions  correct!")
print("You got " +   str((score/3) * 100 )  + "%.")

#string manipulations and  if else statements used