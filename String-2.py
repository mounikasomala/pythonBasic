# 2. Write a python program to accept a string and
#     print only consonants in the given left to right order
 
# solution:
    word = input()
    vowels = "aeiou"
 
    for ch in word:
        if ch not in vowels:
            print(ch)
# Input
# mounika
# Output
# m
# n
# k
