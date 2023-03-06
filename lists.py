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
    arr = 