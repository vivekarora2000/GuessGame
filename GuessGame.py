from random import randint
a = randint(1,10)
guess=[]
i=0;
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