class Solution {
public:
    int minPairSum(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int n = nums.size();
        int i = n / 2 - 1, j = n / 2;
        int maxi = 0;
        while(i >= 0 && j < n){
            maxi = max(maxi,nums[i--] + nums[j++]);
        }
        return maxi;
    }
    
};