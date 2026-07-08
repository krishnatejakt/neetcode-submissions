class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> element_count;
        for(int n: nums)  element_count[n]++;

        vector<vector<int>> freq(nums.size()+1);

        for(auto& [element, count]: element_count) {
            freq[count].push_back(element);
        }

        vector<int> res;

        for (int i = freq.size() - 1; i > 0; i--) {
            for(int e: freq[i]) {
                res.push_back(e);

                if(res.size() >=k) {
                    return res;
                }
            }
        }
        return res;
    }
};
