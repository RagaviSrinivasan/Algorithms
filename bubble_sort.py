#----------------------------------------------------------------------------------------
# Algorithm   : Bubble sort
# Description : For each cycle, compare and swap if left > right, for N-1 cycles
#               At the end of each cycle, largest number will be sorted to the right most
#               index in the unsorted sub-list
# Complexity  : Best - O(N), when list is sorted
#               Average, worst - O(N^2)
#----------------------------------------------------------------------------------------
def BubbleSort(a):
    if not a:
        print "list empty"
    else:
        for i in range(len(a)):
            for j in range(len(a)-i-1):
                if a[j] > a[j+1]:
                    a[j], a[j+1] = a[j+1], a[j]
    print a

a = [1,3,2, 234, 256, 2587, 45789, 244, 5, 97, 5643, 83,98]
BubbleSort(a)