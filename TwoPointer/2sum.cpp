class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        //save the indicies
        //2d-array
        vector<vector<int>>arr;
        for(int i=0;i<nums.size();i++){
            //nums[i],i
            arr.push_back({nums[i],i}); //first enitity will be the value-to sort on first vslue
        }
        //sort the array
        sort(arr.begin(), arr.end()); //sorting the 2d-array

        //two pointer
        int start=0;
        int end=nums.size()-1;
        while (start<end){
            int c_sum=arr[start][0]+arr[end][0];
            if(c_sum==target){
                //return the answer
                return {arr[start][1], arr[end][1]};
            }
            else if(c_sum>target){
                end-=1;
            }
            else{
                start+=1;
            }
        }
        return {};
    }
};

//bruteforce
//nested loops-O(N^2)

//hashmap approach
//map-O(N)->O(N^2)

//two-pointer
