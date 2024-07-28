


def fibo(n):
    a,b = 0,1 #starting sequence;  sum of the two preceding numbers since 1 is start 0 + 1
    fibonnaci = [b] # sequence starts at 1

    for i in range(n):
        a,b=b,a+b # a becomes b , b becomes the sum of the preceding numbers a(before) + b(itself)
        fibonnaci.append(b) 

    return fibonnaci

print(fibo(7))





