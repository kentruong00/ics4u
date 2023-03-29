def stringSort(word):
    arr = list(word)
    flag = True
    while flag:
        action = False
        for i in range(len(arr)-1):
            if arr[i]>arr[i+1]:
                first = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = first
                action = True
        if not action:
            flag = False
    sorted = ''.join(arr)
    print(sorted)