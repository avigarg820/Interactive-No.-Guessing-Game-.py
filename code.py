import random
randm_num = random.randint(1,100)
guesses = 0
userguess = None # means 0
print("#WELCOME PEEPS# To The Guessing Game:--> //WE BELIEVE IN YOU//<--")
while (userguess !=randm_num):
    userguess = int(input('  Your Guess from 1 to 100 "Mon Chere"/ My-Dear:'))
    print()
    if userguess == randm_num:
        print("OUTPUT == *BOLO TARA RARA*","Correct Guess!")
    else:
        print(" Haw, Wrong Guesss","")
        if (userguess>randm_num):            
            
            print(' But Good Going- Enter a SMALLER Number Mon Chere-->')
        else:
            print('  But Going Great SO FAR- Enter a LARGER Number Mon Chere-->')
        print()
    guesses+=1    
print()
print(f"-->It took you abt {guesses} Great guess to reach correct ans!!") 
if guesses <=6:
    print("#PROUDMOMENT")
else:
    print("#IMPROVED&PROUD")
print()     
print("Greetings of congrats on your success with best wishes for your next adventure!”, Good Day")    
