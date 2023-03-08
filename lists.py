# operaters create something new, and methods mutate the list
a_list = [1,2,3,4,5]
b_list = a_list
a_list.append(17)
print(a_list)
print(b_list)
def swapAdj(word: str, target: int) -> str:
    #swap two adjecent letters at given index
    before = word[:target]
    after = word[target+2:]
    swap = word[target+1] + word[target]
    return before + swap + after
print(swapAdj('hello', 1))
def swap(word: str, num1: int, num2: int):
    #swap two latters of a string given 2 index location, num1 and num2
    # arr = 
    return
def mean(array: list) -> int:
    #return the mean of a list 
    if not array: # if len(arr) == 0, for other languages
        return 0
    for i in array:
        total = sum(array)
        return total/len(array)
def median(array: list):
    #return the median value of a list
    if not arraySorted:
        return 0
    # array.sort() # modify/mutates the list, .sort() is a method that belongs to list
    arraySorted = sorted(array) # returns a new list that is sorted
    if len(arraySorted) % 2 == 0:
        mid = len(arraySorted) / 2
        return (arraySorted[mid]+arraySorted[mid-1])/2
    else:
        mid = len(arraySorted) // 2
        return arraySorted[mid]
def mode(array: list):
    max = '0'
    if not array:
        return 0
'''
hi
'''
def sortReverse(word):
    before = word
    sorted = ''
    while before:
        largest = max(before)
        sorted += largest
        before.replace(largest, '')
    return sorted
print(sortReverse('hello'))

