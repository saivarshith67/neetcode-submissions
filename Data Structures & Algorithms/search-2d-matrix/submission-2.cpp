class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
    int m = matrix.size();
    if (m == 0) return false;
    int n = matrix[0].size();

    int s = 0, e = m * n - 1;

    while (s <= e) {
        int mid = s + (e - s) / 2;
        int row = mid / n;
        int col = mid % n;
        int element = matrix[row][col];
        
        if (element == target) return true;
        else if (element < target) s = mid + 1;
        else e = mid - 1;
    }
    return false;

    }
};
