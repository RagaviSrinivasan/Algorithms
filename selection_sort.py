#-----------------------------------------------------------------------------------
# Algorithm   : Selection sort
# Description : For each cycle, find the index of the smallest number in the unsorted
#               sub-list and swap it with the first index of the sorted sub-list
# Complexity  : O(N^2)
#-----------------------------------------------------------------------------------

def SelectionSort(a):
    if not a:
        print "list empty"
    else:
        for i in range(len(a)):
            min_pos = i
            for j in range(i+1, len(a)):
                if a[min_pos] > a[j]:
                    min_pos = j
            a[i], a[min_pos] = a[min_pos], a[i]
    print a
a = [1,3,2,2365,287,236,187,679,42,97]
SelectionSort(a)