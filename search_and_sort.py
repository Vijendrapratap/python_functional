#creating a class for sorting and searching
class SearchAndSort():

    def __init__(self, lst, phrase):
        self.lst = lst
        self.phrase = phrase

    #defining binary search function for searching numbers in given list
    def binarysearch_nmb(self, lst, d):
        lst.sort()
        l = 0
        r = len(lst) - 1
        mid = 0

        #checking conditions
        while r >= l:

            mid = l+ (r - l) // 2

            if lst[mid] > d:
                r = mid - 1

            elif lst[mid] < d:
                l = mid + 1
            else:
                return mid
        else:

            return -1

    #difining binary search method to find word in string
    def binarysearch_word(self, phrase, w):
        phrase1 = phrase.split()
        phrase1.sort()
        l = 0
        r = len(phrase1) - 1

        while r >= l:

            mid = l + (r - l) // 2
            if phrase1[mid] < w :
                l = mid + 1


            elif phrase1[mid] > w:
                r = mid -1

            else:
                return mid

        else:

            return -1

    #defining a insertion sort method for sorting our list
    def insertion_sort_nmb(self, lst):

        for i in lst:
            j = lst.index(i)
            while j > 0:
                if lst[j - 1] > lst[j]:

                    #swap
                    lst[j - 1], lst[j] = lst[j], lst[j - 1]
                else:
                    break
                j = j - 1

        return lst


    #defining bubble sort sort method for sorting
    def bubble_sort_nmb(self, lst):

        for i in range(len(lst)):
            for j in range(len(lst) - 1):
                if lst[j] > lst[j + 1]:
                    #swap
                    lst[j], lst[j + 1] = lst[j + 1], lst[j]
        return (lst)


    #defining insertion sort method for sorting phrase
    def insertion_sort_word(self, phrase):
        phrase1 = phrase.split()

        for i in phrase1:
            j = phrase1.index(i)
            while j > 0:
                if phrase1[j - 1] > phrase1[j]:
                    phrase1[j - 1], phrase1[j] = phrase1[j], phrase1[j - 1]
                else:
                    break
                j = j - 1

        return phrase1

    #defining bubble sort method for sorting phrase
    def bubble_sort_word(self, phrase):
        phrase1 = phrase.split()

        for i in range(len(phrase1)):
            for j in range(len(phrase1) - 1):
                if phrase1[j] > phrase1[j + 1]:
                    phrase1[j], phrase1[j + 1] = phrase1[j + 1], phrase1[j]
        return (phrase1)


list1 = [12, 23, 34, 45, 56, 67, 78, 89, 90, 98, 87, 76, 65, 54, 43, 32, 21]
phrase = "thing of beauty is joy forever"


sos = SearchAndSort(list1, phrase)

#calling our methods for different operations
bubsort1 = sos.bubble_sort_nmb(list1)
print(bubsort1)
insort1 = sos.insertion_sort_nmb(list1)
print(insort1)

bubsort2 = sos.bubble_sort_word(phrase)
print(bubsort2)
insort2 = sos.insertion_sort_word(phrase)
print(insort2)

binsearch_word = sos.binarysearch_word(phrase, "joy")
if binsearch_word != -1:
    print("Element is present at index {}".format(binsearch_word))
else:
    print("Element is not present in list")

binsearch = sos.binarysearch_nmb(list1, 78)
if binsearch != -1:
    print("Element is present at index {}".format(binsearch))
else:
    print("Element is not present in list")





