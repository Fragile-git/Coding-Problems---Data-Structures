
def palindrome(word):
    word2 = word[::-1]
    if word == word2:
        print("It is Palindrome")
    else:
        print("It is not")

palindrome("racecar")
palindrome("racecars")

