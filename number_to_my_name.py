"""
Number to my name 

Given a positive integer, write a program that prints 
each digit of the number as its corresponding word starting 
from the ones digit. The program should support numbers from 
0 to 9 for their word representations:
• 0: ZERO
• 1: ONE
• 2: TWO
• 3: THREE
• 4: FOUR
• 5: FIVE
• 6: SIX
• 7: SEVEN
• 8: EIGHT
• 9: NINE

"""
name = ['ZERO','ONE','TWO','THREE','FOUR','FIVE','SIX','SEVEN','EIGHT','NINE']

number = input('Enter number: ')
print('Word representation of the number: ')

for i in number[::-1]: # reverse the input, to start at ones place
    #iterate over the numerical string
    for index,value in enumerate(name):    
        if int(i) == index: # convert the string into int 
            print(value)

    












