from typing import List, Set # this adds type hints for List and Set

def list_to_set(nums: List[int]) -> Set[int]:
    #my_set is declaring it as the set 
    my_set = set()
    #for loop in n nums 
    for n in nums:
        #this would n into set 
        my_set.add(n)
        #this would return the set with the numbers
    return my_set 
# do not modify below this line
print(list_to_set([1, 2, 3, 4, 5]))
print(list_to_set([1, 1, 2, 2, 3, 3]))
print(list_to_set([1, 2, 3, 4, 5, 5, 5, 3, 4, 5]))
