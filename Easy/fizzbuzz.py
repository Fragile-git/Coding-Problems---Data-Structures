"""
FizzBuzz:
Write a program that outputs the string representation of numbers from 1 to N, 
but for multiples of 3 it should output "Fizz" instead of the number and for 
the multiples of 5 output "Buzz". For numbers which are multiples of both three 
and five, output "FizzBuzz".

"""

num = int(input("Enter a positive integer n: "))

def fizzbuzz(num):
    print(f'FizzBuzz sequence from 1 to {num}: ')
    for i in range(1,num+1):
        if (i % 3) == 0 or (i % 5) == 0:
            if (i % 3) == 0:
                print("Fizz", end ='')
            if (i % 5) == 0: 
                print("Buzz", end = '')
            print(end=' ')
        else:
            print(i, end= ' ')
fizzbuzz(num)

print()

def fizzbuzz_better(num):

    for i in range(1,num+1):
        word =''

        if (i%3) == 0:
            word += 'FIZZ'
        if (i%5) == 0:
            word += 'BUZZ'
    
        print(word or i, end=" ") # chooses to print the truthful value word or i 
        # if word is empty it chooses to print the i 
        # if "i" is put first "i" will evaluate to true since its a non-zero value thus it will always be printed

fizzbuzz_better(num)

