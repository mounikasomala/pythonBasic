# 1. Write a python program to accept a string and 
#     print alternate characters starting 
#     from first character
 
# solution:
    word = input()
    n = len(word)
    for index in range(0, n, 2):
        print(word[index], end = " ")

# Input
# mounika
# Output
# m u i a 
