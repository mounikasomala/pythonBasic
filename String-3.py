# 3. Write a python program to accept a string and 
#     print whether it is a palindrome or not
 
# solution:
    word = input()
    reverseWord = word[::-1]
    if word == reverseWord:
        print("Palindrome")
    else:
        print("Not a palindrome")
# Input
# malayalam
# program 
# Output
# palindrome
# Not a palindrome
