from random import randint
a = randint(1,100)
print("WELCOME TO GUESS ME!")
print("I'm thinking of a number between 1 and 100")
print("If your guess is more than 10 away from my number, I'll tell you you're COLD")
print("If your guess is within 10 of my number, I'll tell you you're WARM")
print("If your guess is farther than your most recent guess, I'll say you're getting COLDER")
print("If your guess is closer than your most recent guess, I'll say you're getting WARMER")
print("LET'S PLAY!")
guess=[]
while True:
    g=int(input('Enter Guess:'))
    guess.append(g)
   
    if a==g:
            print('Got it ')
            break
    if (abs(a-g)<=10):
            print('Warm')
    if (abs(a-g)>10):
            print('Cold') 
    
    if (len(guess)>1):
        b=guess[-2]
        if(abs(a-g)<abs(a-b)):
            print('Warmer')
        if(abs(a-g)>abs(a-b)):
            print('Colder')
    pass
print(len(guess))