class Solution {
   public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int i = 0;

        unordered_map<int, int> two_sum;

        for (int num : nums) {
            if (two_sum.contains(target - num)) {
                return {two_sum[target - num], i};
            }
            two_sum[num] = i;
            i += 1;
        }
    }
};
