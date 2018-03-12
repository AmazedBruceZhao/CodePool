import time
import numpy as np
import random
#generate test array
def generateArray(length, start, end):
    return np.random.randint(start, end, size=(length, ))

def swap(array, x, y):
    if(x == y): return
    if(array[x] == array[y]): return
    temp = array[x]
    array[x] = array[y]
    array[y] = temp

#O(n^2)
def selectionSort(array):
    n = len(array)
    for i in range(n):
        min = i
        for j in range(i + 1, n):
            if(array[j] < array[min]):
                min = j
        swap(array, i, min)

#O(n^2) 
#O(n) when the list is almost sequential
def insertSort(array):
    n = len(array)
    for i in range(1, n):
        #j = i
        #while(j > 0):
        target = i
        copy = array[i]
        for j in range(i, 0, -1):

            if(copy < array[j - 1]):
                array[j] = array[j -1]
                target = j - 1
                #j -= 1
            else:
                #array[j -1] = copy
                break
        if(target != i):
            array[target] = copy


def mergeSort(array, left, right):
    if(left >= right):
        return
    mid = (left + right)/2
    mergeSort(array, left, mid)
    mergeSort(array, mid + 1, right)
    #optimize
    #merge is needed only when mid > mid + 1
    #left and right array is supposed to be ordered respectively
    if(array[mid] > array[mid + 1]):
        merge(array, left, mid, right)

#mergesort from bottom to up
#no need to define left and right, suitable for linked list
def mergeSortBU(array):
    n = len(array)
    size = 1
    while(size < n):
        #log(n) times
        for i in range(0, n - size + 1, size * 2):
            #left: i : i + size - 1
            #right: i + size : i + size + size - 1
            merge(array, i, i + size - 1, min((i + size * 2 - 1, n - 1)) )
        size += size


def merge(array, left, mid, right):
    #copy array!!!!
    temp = np.copy(array[left : right + 1])
    l = left
    r = mid + 1
    for i in range(left, right + 1):
        #overflow happens on left or right array
        if(l > mid):
            array[i] = temp[r - left]
            r += 1
            continue

        if(r > right):
            array[i] = temp[l - left]
            l += 1
            continue
        #normal case
        if(temp[l - left ] < temp[r - left]):
            array[i] = temp[l - left ]
            l += 1
        else:
            array[i] = temp[r - left]
            r += 1


def quickSort(array, left, right):
    if(left >= right):return
    t = partition(array, left, right)
    quickSort(array, left, t - 1)
    quickSort(array, t + 1, right)


def partition(array, left, right):
    # optimize with random seed: swap left digit with random seed
    r = random.choice(range(left, right + 1))
    swap(array, left, r)

    # optimize for common-number-duplicate cases
    seed = array[left]
    smaller = left + 1
    bigger = right

    try:
        while(True):
            while(smaller <=  bigger and array[smaller] < seed): smaller += 1
            while( bigger >= smaller and array[bigger] > seed): bigger -= 1
            if (smaller >= bigger): break
            swap(array, smaller, bigger)

            smaller += 1
            bigger -= 1
    except:
        print('err')

    swap(array, left, bigger)
    return smaller - 1

#deeper optimization for large amount of common number
def quickSort3Ways(array, left, right):
    if (left >= right): return

    #partition:
    r = random.choice(range(left, right + 1))
    swap(array, left, r)

    seed = array[left]
    smaller = left
    bigger = right
    i = left + 1

    while(i <= bigger):
        if(array[i] < seed):
            swap(array, i, smaller + 1)
            smaller += 1
            i += 1
        elif(array[i] > seed):
            swap(array, i, bigger)
            bigger -= 1
        else:
            i += 1
    swap(array, left, smaller)
    quickSort3Ways(array, left, smaller - 1)
    quickSort3Ways(array, bigger + 1, right)







def runAlgo():
    length = 6
    start = 0
    end = 10000
    array = generateArray(length, start, end)

    print array
    start = time.time()
    # test algo
    #selectionSort(array)
    #insertSort(array)
    #mergeSort(array, 0, len(array) - 1)
    #mergeSortBU(array)
    #quickSort(array, 0, len(array) - 1)
    quickSort3Ways(array, 0, len(array) - 1)
    #np.sort(array)
    duration = time.time() - start
    print array
    print duration

runAlgo()








