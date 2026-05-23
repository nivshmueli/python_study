def course_schedule_alg(prerequisites, numCourses):

    #build connectivity description
    connnactivity = [[] for _ in range(numCourses)] 
    for edge in prerequisites:
       connnactivity[edge[1]].append(edge[0])

    
    def test_loop(cur_c):
    
        if  cur_c == course:
            return False
        
        for next_c in connnactivity[cur_c]:
           ret =  test_loop(next_c)
           if ret ==False:
               return False

    
    # for each coarse check if ther is a loop back to the coarse
    for course in range(numCourses):

        ret = test_loop(course)
        if ret==False:
            return False
        
    return True
