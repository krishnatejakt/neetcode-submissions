class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        map<int,int> duplicates;

        for(int num: nums) {
            duplicates[num]+=1;
            if(duplicates[num]>1) {
                return true;
            }
        }
        return false;
    }
};