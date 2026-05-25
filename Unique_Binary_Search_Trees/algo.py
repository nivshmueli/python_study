 


def unique_binary_search_trees(start, end):

    if  start > end:
        return 0
    
    if start == end:
        return 1
    
    cur_sum = 0
    for split in range(start,end):
        cur_sum = cur_sum + \
                  unique_binary_search_trees(start, split-1) + \
                  unique_binary_search_trees(split + 1, end)
        
    return cur_sum
    




if __name__ == "__main__":
    n=3
    print(unique_binary_search_trees(1,n))