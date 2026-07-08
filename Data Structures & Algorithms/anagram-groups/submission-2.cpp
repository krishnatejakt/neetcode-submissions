class Solution {
   public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        
        map<vector<int>, vector<string>> anagrams;

        for (string str : strs) {
            vector<int> vect(26,0);

            for (char x : str) {
                vect[int(x) - int('a')] += 1;
            }

            anagrams[vect].push_back(str);
        }

        vector<vector<string>> result;

        for (const auto& [key, value] : anagrams) {
            result.push_back(value);
        }

        return result;
    }
};
