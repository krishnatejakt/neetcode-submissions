class Solution {
public:
    bool isAnagram(string s, string t) {

        if(s.size()!=t.size()) return false;
        
        vector<int> vect(26);



        for(char x: s){
            vect[int(x) - int('a')]+=1;
        }

        for(char y: t) {
            vect[int(y) - int('a') ]-=1;
        }

        for(int x: vect) {
            if(x!=0){
                return false;
            }
        }

        return true;
        
    }
};
