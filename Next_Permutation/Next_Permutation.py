
import numpy as np

def next_permutation(perm_in):

    perm_in = np.array(perm_in)

    last=len(perm_in-1)


    for i in range(last,1,-1):
        if perm_in[i-1] < perm_in[i]:
            # in the range i to the end
            #fsort up the range perm_in[i-1 to end]
            sorted_left = sort_up(perm_in[i-1:-1])

            # find  perm_in[i-1] im=n the sorted list and thake the next location: loc
            perm_in[i-1] = sorted_left[loc]

            np.delete(sorted_left, )

            perm_in[i:-1] = 
        