# 5. Write a python program to accept string and print 
#     total number of "ab" substring present in given string
  
# solution
word = input()
result = 0 
n = len(word)
# n = 8
 
for index in range(n - 1):
    if word[index] == 'a' and word[index + 1] == 'b':
        result += 1  
print(result)
# Input
# # freabsdabsdaab 
# Output
# # 3
 
