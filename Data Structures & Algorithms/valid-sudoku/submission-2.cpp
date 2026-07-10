class Solution {
   public:
    bool isBoard(vector<char>& row) {
        unordered_map<char, int> check;

        for (char ch : row) {
            if (check[ch] == 1 && ch != '.') {
                return false;
            }
            check[ch] = 1;
        }

        return true;
    }

    bool isValidSudoku(vector<vector<char>>& board) {
        bool isResult = true;

        vector<char> row(9, '.');
        int j = 0;

        while (j < 9) {
            for (int i = 0; i < 9; i++) {
                row[i] = board[j][i];
            }

            isResult = isBoard(row);

            if (isResult == false) {
                return false;
            }

            vector<char> row(9, '.');

            j += 1;
        }

        int a = 0;

        vector<char> col(9, '.');

        while (a < 9) {
            for (int i = 0; i < 9; i++) {
                col[i] = board[i][a];
            }
            isResult = isBoard(col);
            if (isResult == false) {
                return false;
            }

            vector<char> col(9, '.');
            a += 1;
        }

        set<int> range = {0, 3, 6};

        vector<char> test(9, '.');
        int m = 0;

        for (int i : range) {
            for (int j : range) {
                m = 0;
                for (int k = i; k < i + 3; k++) {
                    for (int l = j; l < j + 3; l++) {
                        test[m] = board[k][l];
                        m += 1;
                    }
                }
                isResult = isBoard(test);
                if (isResult == false) {
                    return false;
                }

                vector<char> test(9, '.');
                
            }
        }

        return isResult;
    }
};
