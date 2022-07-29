from random import randint

#random array for testing
def create_array(size = 10, max = 50):
    return [randint(0,max) for _ in range(size)]

# applies quicksort to input array in place

def partition(a, low, high): # partition divides the array into two parts

    i = low -1
    pivot = a[high]
    for j in range(low,high):
        if a[j] <= pivot:
            i += 1
            a[i],a[j] = a[j],a[i]  
    a[i+1],a[high] = a[high],a[i+1]
    return i+1

def quicksort(a, low=0, high=None):
    if high == None:
        high = len(a)-1
    if low < high:
        p_idx = partition(a, low, high) # partition around pivot
        quicksort(a,low, p_idx -1) # sort lower half
        quicksort(a, p_idx+1,high) # sort upper half

a = create_array()
print ("unsorted array:" , a)
quicksort(a)
print("sorted array", a)
