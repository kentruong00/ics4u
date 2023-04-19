from random import randrange
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
def factors(num):
    stopping = int(num**0.5)
    return 
def randomGen(low, high, amount):
    from random import randrange
    return [randrange(low,high) for _ in range(amount)]
def palindromeThreeDigits():
    largest = 0
    for i in range(999,99,-1):
        for j in range(999,99,-1):
            arr = list(str(i*j))
            if arr == arr[::-1] and i*j>largest:
                largest = i*j
                max = len(arr)
    return largest
'''
hi
'''
def twoSum(nums, target):
    dict = {}
    for i in range(len(nums)):
        if target - nums[i] in dict:
            return [dict[nums[i]],i]
        dict[nums[i]] = i
<<<<<<< HEAD
<<<<<<< HEAD:lists.py
    return []
def maxArea():
    return


def sortReverse(num):
    arr = [randrange(1,10) for i in range(num)]
    print (arr)
    arr.sort()
    return arr[::-1]

=======
    return 
>>>>>>> 59e32d1d0f5521ec3e6975b7ee25688f45403a28:grade 11 review/lists.py
=======
    return 
>>>>>>> 59e32d1d0f5521ec3e6975b7ee25688f45403a28
