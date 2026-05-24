


import string

def Longest_Substring_Without_Repeating_Characters(in_string):


    first = 0
    last  = 1
    max_size = 1

    letter_dict = {letter: False for letter in string.ascii_lowercase}

    letter_dict[in_string[0]] = True

    while(last < len(in_string)):
        
        if letter_dict[in_string[last]]: 

            if last == len(in_string) - 1:
                break

            while letter_dict[in_string[last]] == True:
                first = first + 1
                letter_dict[in_string[first]] = False

        max_size = max(max_size,last - first + 1) 
        letter_dict[in_string[last]] = True
        last = last + 1

    return max_size


if __name__ == "__main__":
    s = "abcabcbb"

    print( Longest_Substring_Without_Repeating_Characters(s) )