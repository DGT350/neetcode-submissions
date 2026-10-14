class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        //variable to set the count = 0 
        int count = 0;
        //varibale used to store the amount of numbers seen 
        int res = 0;
        //for loop to traverse through the array
        for(int i = 0; i < nums.size(); i++){
            //if the number equals to one
            if(nums[i] == 1){
                //counts the number of 1 seen
                count++;
                //compares the previous consecutive numbers seen to 1 to the current
                res = max(res,count);
                //if a zerro is seen then it sets the count back to zero            
            }
            else{
                
                count = 0;
            }
        }
        // resturns the consecutive number of 1s seen 
        return res;
    }
};