class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int l = 0;
        int r = numbers.size() - 1;
        vector<int> ans;
        while(l < r) {
            int currSum = numbers[l] + numbers[r];
            if(currSum == target) {
                ans.push_back(l + 1);
                ans.push_back(r + 1);
                break;
            }
            else if(currSum > target) {
                r--;
            } else {
                l++;
            }
        }

        return ans;
    }
};
