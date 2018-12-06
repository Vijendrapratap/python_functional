
#defining a function for permutaion
def permutations(lst, r=''):
    if len(lst) == 0:
        print(r)
    else:
        for i in range(len(lst)):

            #recursive function
            permutations(lst[0:i] + lst[i + 1:], r + lst[i])

#user input
permutations("abcd")



