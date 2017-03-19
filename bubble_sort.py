def BubbleSort(a):
    if not a:
        print "list empty"
    else:
        for i in range(len(a)-1,0,-1):
            for j in range(i):
                if a[j] > a[j+1]:
                    a[j], a[j+1] = a[j+1], a[j]
    print a

a = [1,3,2, 234, 256, 2587, 45789, 244, 5, 97, 5643, 83,98]
BubbleSort(a)