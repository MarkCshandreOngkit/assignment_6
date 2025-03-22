#input statement
statement = input("Input: ")

#check number of words
#split statement to words
number = 0
words = statement.split()
#iterate through each word
for word in words:
    #add 1 per word
    number += 1
#print number of words
print(number)

