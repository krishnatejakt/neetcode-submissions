class Solution {
public:
    bool isAnagram(string s, string t) {
        map<char, int> characters;

        for(char x: s) {
            characters[x]+=1;
        }

        for (char y: t) {
            characters[y]-=1;
        }

        for (const auto& [character, count]: characters) {
            if(count!=0){
                return false;
            }
        }

        return true;
    }
};
