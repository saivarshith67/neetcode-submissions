class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int> seen;

        int n = nums.size();

        for (int i = 0; i < n; i++)
        {
            int curr = nums[i];
            if (seen.find(curr) != seen.end())
            {
                // element is present in set => duplicates are present
                return true;
            }
            else
            {
                // element not present in set, add it
                seen.insert(curr);
            }
        }

        return false;
    }
};
