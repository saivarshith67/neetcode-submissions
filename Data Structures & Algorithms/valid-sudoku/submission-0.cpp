class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        // Hash sets to track seen digits in rows, columns, and boxes
        unordered_set<char> rowSet, colSet, boxSet;

        for (int i = 0; i < 9; i++) {
            rowSet.clear();
            colSet.clear();
            for (int j = 0; j < 9; j++) {
                // Check row
                char rowVal = board[i][j];
                if (rowVal != '.') {
                    if (rowSet.count(rowVal)) return false;
                    rowSet.insert(rowVal);
                }

                // Check column
                char colVal = board[j][i];
                if (colVal != '.') {
                    if (colSet.count(colVal)) return false;
                    colSet.insert(colVal);
                }
            }
        }

        // Check 3x3 sub-boxes
        for (int boxRow = 0; boxRow < 3; boxRow++) {
            for (int boxCol = 0; boxCol < 3; boxCol++) {
                boxSet.clear();
                for (int i = 0; i < 3; i++) {
                    for (int j = 0; j < 3; j++) {
                        char val = board[boxRow * 3 + i][boxCol * 3 + j];
                        if (val != '.') {
                            if (boxSet.count(val)) return false;
                            boxSet.insert(val);
                        }
                    }
                }
            }
        }

        return true;
    }
};
