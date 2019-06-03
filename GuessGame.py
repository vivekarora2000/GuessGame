from random import randint
a = randint(1,10)
print("WELCOME TO GUESS ME!")
print("I'm thinking of a number between 1 and 100")
print("If your guess is more than 10 away from my number, I'll tell you you're COLD")
print("If your guess is within 10 of my number, I'll tell you you're WARM")
print("If your guess is farther than your most recent guess, I'll say you're getting COLDER")
print("If your guess is closer than your most recent guess, I'll say you're getting WARMER")
print("LET'S PLAY!")
guess=[]
while True:
    g= int(input("I'm thinking of a number between 1 and 100.\n  What is your guess? "))
    
    if g < 1 or g > 100:
        print('OUT OF BOUNDS! Please try again: ')
        continue
    
    if g == a:
        print(f'CONGRATULATIONS, YOU GUESSED IT IN ONLY {len(guess)} GUESSES!!')
        break

    guess.append(g)

    if len(guess)>1 and guess[-2]:  
        if abs(a-g) < abs(a-guess[-2]):
            print('WARMER!')
        else:
            print('COLDER!')
   
    else:
        if abs(a-g) <= 10:
            print('WARM!')
        else:
            print('COLD!')
