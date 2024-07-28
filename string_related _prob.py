


# Removes duplicate in a word 
str1 = input("Input a word: ")
word = ""# needs to explicitly declared
for i in str1:
    if i not in word: # if 
        word += i # when using assignment operators
print(word)


''' # method 2
for i in str1:
    if i not in list1:
        list1.append(i)a

for x in range(len(list1)):
    print(list1[x], end = '')
'''

# String Sort: 

"""
In this problem you will need to sort a list of words based on their length. 
The shortest word must be first and the longest word must be last. Words of the 
same length may be in any order within that length. 

Given the list of words: 
fourteen, forty, thirty, one, three, the sorted list will be: one, forty, three, 
thirty, fourteen.


"""
num = int(input("Enter count of words: "))
words = []
for i in range(num):
    enter = input("Enter next word: ")
    words.append(enter)

sorted_words = sorted(words, key=len) # sort based on function len 
print(sorted_words)




