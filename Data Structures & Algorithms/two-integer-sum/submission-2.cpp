class Solution {
   public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int i = 0;

        map<int, int> two_sum;
        vector<int> vect(2);

        for (int num : nums) {
            if (two_sum.contains(target - num)) {
                vect[0] = two_sum[target-num];
                vect[1] = i;
                return vect;
            }
            two_sum[num] = i;
            i += 1;
        }
    }
};
