# Strings are a data type that is a sequence of characters
# created by enclosing characters in double or single quotes

# Comparing strings
'Jake' < 'Jane' # Evaluates to true
# First two letters are the same but 'n' has a higher ascii value than 'k'
#  Iterating a string
word = 'hello'
i = 0
while i < len(word):
    print(word[i])
    i += 1
# variable represents the index
for c in word:
    print(c)
# variable represents the actual character
# String slicing
# string[start:end (non inclusive): step], the end and start value can be greater or equal to the length of the string, will not return an error
# step = 1 if not specified
print(word[:4]) # when the start is not specified start at the beginning
print(word[2:]) # when end is not specified it goes until the end of the string
print(word[::-1]) # reverse the string, implied start and end, step of -1
# Strings are immutable, the data type can't be altered without being recreated
'''
name = 'Jim'
name[0] = 'T' will produce an error
'''
# Slicing and indexing create strings:
'''
word = 'hello'
newWord = word[2:]
slicing the string creates a new string from the original word
newWord is a subset of the original string
'''

# String casting, any data type can be turned into a string
def swap(word, num1, num2):
    #swap two letters, num1 is the index of the first letter and num2 is the index of the second letter
    before = word[:num1]
    after = word[num2+1:]
    between = word[num1+1:num2]
    return before + word[num2] + between + word[num1] + after
print(swap('hello',0,4))
