

def find_3sum(integer_list):

# sort the array

# fimd the location with the first posetive (first_posetive) number so
# you can logically use the positive or negative array 


# 
triplate_1=find_3sum_pos_neg(integer_list,0,first_posetive-1,first_posetive,in_l)
triplate_2=find_3sum_pos_neg(integer_list,first_posetive,in_l,0,first_posetive-1)


def find_3sum_pos_neg(integer_list,stsrt_one_num,end_one_num,stsrt_two_num,end_two_num):


#loop over all possibole numbeer in one buffer
    for i in arange(stsrt_one_num,end_one_num+1):

        big_num=integer_list[i]

        # find the limit so that the two number that are added as oposite to one 
        # number must not be bigger then the one number
        for i in arange(stsrt_two_num,end_two_num):
            if integer_list[i] > -big_num:
                
                if stsrt_one_num >=0:
                    stsrt_two_num=i
                else:
                    end_two_num=i

                break

        #work with two pointers to find the sum of the two number that equal the one number
            
            