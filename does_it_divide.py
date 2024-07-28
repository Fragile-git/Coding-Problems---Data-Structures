"""
Consider a permutation of numbers from 1 to N (1,2,3,4,5,6,7,N) written on a paper. 
Let's denote the product of its element as 'prod' and the sum of its elements as 'sum'. 
Given a positive integer N, your task is to determine whether 'prod' is divisible by 'sum' or not.

Input Format: First input will be an integer T.  It depicts a number of test cases. 

Each test case will contain an integer N (1<= N <=10^9). It is nothing but the length of the permutation.


Ex: 2 then (1*2)/(1+2)
    3 then (1*2*3)/(1+2+3)

"""


size = int(input())
arr=[]
for i in range(0,size):
    arr.append(int(input()))
 
for n in arr:
    if (n>=1) and (n<=10**9): # checks if input fits the category: 1<= N <=10^9
        prod = 1
        summ = 0
        for i in range(1,n+1): # since permutation starts at 1 
            prod *=i
            summ +=i
        if prod%summ==0:
            print("YEAH")
        else:
            print("NAH")
