class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int prefix = 1;
        int n = nums.size();

        vector<int> result(n, 1);

        for(int i = 0 ; i< n; i++) {
            result[i]*=prefix;
            prefix*=nums[i];
        }

        int postfix = 1;

        for(int j = n - 1; j>=0; j--) {
            result[j]*=postfix;
            postfix*=nums[j];
        }
        
    return result;
    }
};
