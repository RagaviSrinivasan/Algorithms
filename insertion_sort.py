#----------------------------------------------------------------------------------------
# Algorithm   : Insertion sort
# Description : Take the left most element of the unsorted list and
#               swap it in order in the sorted list, adding one element to the sorted list
                at the end of each cycle
# Complexity  : Best - O(N), when list is sorted
#               Average, worst - O(N^2)
#----------------------------------------------------------------------------------------
def InsertionSort(a):
    if not a:
        print "list empty"
    else:
        for i in range(len(a)):
            for j in range(i):
                if a[i] < a[j]:
                    a[i], a[j] = a[j], a[i]
    print a

a = [54, 26, 93, 17, 77, 31, 44, 55, 20]
InsertionSort(a)