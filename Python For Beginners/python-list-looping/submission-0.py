from typing import List # used to add type hint for List

def count_x(nums: List[int], x: int) -> int:
    # a counter to count how many the number is seen
    count = 0
    # a for loop to traverse through the loop 
    for num in nums:
        #if the number is seem
        if num == x:
            #update the counter 
            count += 1 
        #retrun the number of times the number was seen 
    return count 


# do not modify below this line
print(count_x([1, 2, 5, 6, 5], 5))
print(count_x([4, 3, 6, 1, 6], 5))
print(count_x([4, 7, 7, 6, 7, 6], 7))
