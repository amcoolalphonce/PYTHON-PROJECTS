def give_options(x, y, z):
    print("A  :", x)
    print("B  :", y)
    print("C  :", z)

print('''
HELLO ! , WELCOME TO MY QUIZ
EVERY ANSWER IS WORTH 10 POINTS   ''')
#define a variable for user input

ans=input('ARE YOU READY TO PLAY THE GAME YES/NO    :')
disc='NOTE: Write the actual answer ,NOT the option'
score=0                          #initial score is zero before you start.this is very important
total_questions=5
# answers=('Python', ' ')      you can predefine all those answers

if ans.lower()=='yes':
    print(disc)
    print('What is the best programming language    :')
    give_options('Python', 'C++', 'Java')
    ans=input('My answer is  :')

    if ans.lower()=="python":     #answers[0]
        score+=1                  #score=score+1// incrementing
        print('COREECT ')
    else:
        print('INCORRECT')
    print('.........................................')
    print(disc)
    print('Who is the founder of APLE    :')
    give_options('Mark Zuckerbeg', 'Bill Gates', 'Steve Jobs')
    ans=input('My answer is  :')

    if ans.lower()=="steve jobs":     #answers[0]
        score+=1                 #score=score+1// incrementing
        print('COREECT ')
    else:
        print('INCORRECT')
    print(".......................................")
    print(disc)
    print('Which one is a mammal   :')
    give_options('Dog', 'Snake', 'Aligator')
    ans=input('My answer is  :')

    if ans.lower()=="dog":     #answers[0]
        score+=1                #score=score+1// incrementing
        print('CORRECT ')
    else:
        print('INCORRECT')

    print(disc)
    print('Who killed Goliath    :')
    give_options('Moses', 'Hosea', 'David')
    ans=input('My answer is  :')

    if ans.lower()=="david":     #answers[0]
        score+=1                 #score=score+1// incrementing
        print('CORRECT ')
    else:
        print('INCORRECT')

    print(disc)
    print('Which one is a non living thing    :')
    give_options('Stool', 'Bill Gates', 'Steve Jobs')
    ans=input('My answer is  :')

    if ans.lower()=="stool":     #answers[0]
        score+=1               #score=score+1// incrementing
        print('COREECT ')
    else:
        print('INCORRECT')

    i=score*10
    if i<20:
        print(f" YOUR SCORE IS : {i} /50. Better luck next time!")
    elif i==50 :
        print(f'PERFECT!. Your scored is {i}/ 50. EXCELLENT')
    else:
        print(f'Nice try . you scored {i}/ 50')