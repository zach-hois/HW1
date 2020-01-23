import numpy as np

def pointless_sort(x):
    """
    This function always returns the same values to show how testing
    works, check out the `test/test_alg.py` file to see.
    """
    return np.array([1,2,3])

def bubblesort(x):
    """
    Describe how you are sorting `x`
    x will be sorted by comparing the first number to the second and putting them in numerical order
    next, the second will be compared to the third and the switch repeated (if necessary)
    The largest numbers will therefore "bubble" up to the end of the vector
    """
    n = len(x) #length of the submitted array

    for i in range(n): #initialize the for loop for the algorithm so it will run until everything is sorted

        for j in range(0, n-i-1):
            #this loop is the function that will actually change the numbers in the array (x) around
            #The range counts from 0 to length of x minus 1, then once sorted x minus 2, then minus 3.. etc
            if x[j] > x[j+1]:
                x[j], x[j+1] = x[j+1], x[j]
                #IF the number before is greater than the next number, switch their order

    return x

def insertsort(x):
    """
    Describe how you are sorting `x`
    Take our array and split into a sorted (originally n=1) and unsorted sub array
    Take the first "unsorted" and move into sorted, compare to immediate left
    If new item is lower than left, swap them. If higher, its correct
    """
    n = range(1, len(x))
    for i in n:
        needs_sorting = x[i] #new value soon to be added to the sorted list
        
        while x[i-1] > needs_sorting and i>0: #item to left is larger than to right
            x[i], x[i-1] = x[i-1], x[i] #swap the values
            i = i - 1 #step down the list through the index
    return x #sorted array


def quicksort(x):
    """
    Describe how you are sorting `x`
    We take one item from the array and make it our "pivot point"
    iterating through an array, if a number is smaller than the pivot it goes into a new low array
    if the number is higher than the pivot we store it as "higher"
    The same method is applied to these two new arrays until all are sorted
    """
    n = len(x)
    if n <= 1: #if the list is only one or 0 characters, no sorting needed, simply return
        return x
    else: #for everything else...
        pivot = x.pop() #pivot can be any number in the array but ill use built in pop 
        #that takes the last number of array and returns it
        higher = []
        lower = [] #empty arrays that go around the pivot
        
        for i in x:
            if i > pivot: #if i is greater than pivot, add to higher
                higher.append(i)
                
            else:  #if i is lesser (or equal to) add to lower
                lower.append(i)
                
    return quicksort(lower) + [pivot] + quicksort(higher) #return







