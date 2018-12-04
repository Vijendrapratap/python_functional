#defining a merge sort function
def mergesort(lst):

    #dividing list into smaller list
    if len(lst) > 1:
        mid = len(lst)//2
        L = lst[:mid]
        R = lst[mid:]

        mergesort(L)
        mergesort(R)

        i = j = k = 0

        #updating list by comparing two sorted list
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                lst[k] = L[i]
                i += 1

            else:
                lst[k] = R[j]
                j += 1
            k += 1

        # swaping remaining elements
        while i < len(L):
            lst[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            lst[k] = R[j]
            j += 1
            k += 1

    return lst

arr = [102, 117, 713, 554, 576, 857]

#calling function
t = mergesort(arr)
print("sorted array is :",t)


