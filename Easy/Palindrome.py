
"""
Palindrome when it reads the same forward and backward.
"""
def palindrome(word):
    if word == word[::-1]:
        print("It is Palindrome")
    else:
        print("It is not")

palindrome("racecar")
palindrome("racecars")

def isPalindrome(x):
    if str(x) == str(x)[::-1]:
        print("It is Palindrome")
    else:
        print("It is not")


isPalindrome(101)
isPalindrome(-121)
isPalindrome(10)

