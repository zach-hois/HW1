import numpy as np
from example import algs

def test_pointless_sort():
    # generate random vector of length 10
    x = np.random.rand(10)

    # check that pointless_sort always returns [1,2,3]
    assert np.array_equal(algs.pointless_sort(x), np.array([1,2,3]))

    # generate a new random vector of length 10
    x = np.random.rand(10)

    # check that pointless_sort still returns [1,2,3]
    assert np.array_equal(algs.pointless_sort(x), np.array([1,2,3]))

def test_bubblesort():
    # Actually test bubblesort here. It might be useful to think about
    # some edge cases for your code, where it might fail. Some things to
    # think about: (1) does your code handle 0-element arrays without
    # failing, (2) does your code handle characters?

    x = [9,8,7,6,5,4,3,2,1] #regular list
    x1 = [] #empty list
    x2 = ["b","c","a", "d", "z", "a", "c", "h"] #will it sort characters?
    x3 = [5,7,1,5,0,2,5,7,5,5,5,8657] #how does it handle duplicates?

    
    # for now, just attempt to call the bubblesort function, should
    # actually check output
    
    assert algs.bubblesort(x)==[1,2,3,4,5,6,7,8,9]
    assert algs.bubblesort(x1)== []
    assert algs.bubblesort(x2)== ['a', 'a', 'b', 'c', 'c', 'd', 'h', 'z']
    assert algs.bubblesort(x3)== [0, 1, 2, 5, 5, 5, 5, 5, 5, 7, 7, 8657]

def test_insertsort():
    # Actually test bubblesort here. It might be useful to think about
    # some edge cases for your code, where it might fail. Some things to
    # think about: (1) does your code handle 0-element arrays without
    # failing, (2) does your code handle characters?

    x = [9,8,7,6,5,4,3,2,1] #regular list
    x1 = [] #empty list
    x2 = ["b","c","a", "d", "z", "a", "c", "h"] #will it sort characters?
    x3 = [5,7,1,5,0,2,5,7,5,5,5,8657] #how does it handle duplicates?
    
    # for now, just attempt to call the bubblesort function, should
    # actually check output
    algs.bubblesort(x)
    algs.bubblesort(x1) 
    algs.bubblesort(x2) 
    algs.bubblesort(x3)   

def test_quicksort():

    x = [9,8,7,6,5,4,3,2,1] #regular list
    x1 = [] #empty list
    x2 = ["b","c","a", "d", "z", "a", "c", "h"] #will it sort characters?
    x3 = [5,7,1,5,0,2,5,7,5,5,5,8657] #how does it handle duplicates?
    # for now, just attempt to call the quicksort function, should
    # actually check output
    algs.quicksort(x)
    algs.quicksort(x1)
    algs.quicksort(x2)
    algs.quicksort(x3)
