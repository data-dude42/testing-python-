def factorial(number):
    if number==0 or number==1 :
        return 1
    return (number * factorial(number-1))
#if number ==0 or number ==1 

def linear_search(list, key, index=0):
    len_list = (len(list) - 1)
    if(list[index] == key):
        return index
    if((index == len_list) and (list[index] != key)):
        return -1
    return linear_search(list, key, index + 1)
    
    

def binary_search(list, key, low=0, high=None):
    if (high == None):
        high = (len(list) - 1)

    mid = ((low + high) // 2)

    if (low  > high):
        return -1

    if (list[mid] == key):
        return mid
    elif (key > list[mid]):
        return binary_search(list, key, (mid+1), high)
    else:
        return binary_search(list, key, low, (mid-1))
