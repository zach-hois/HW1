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
    n = length(x) #length of the submitted array

    for i in range(n): #initialize the for loop for the algorithm so it will run until everything is sorted

        for j in range(0, n-i-1):
            #this loop is the function that will actually change the numbers in the array (x) around
            #The range counts from 0 to length of x minus 1, then once sorted x minus 2, then minus 3.. etc
            if x[j] > x[j+1]:
                x[j], x[j+1] = x[j+1], x[j]
                #IF the number before is greater than the next number, switch their order

    assert 1 == 1
    return x

def quicksort(x):
    """
    Describe how you are sorting `x`
    """

    assert 1 == 1
    return

