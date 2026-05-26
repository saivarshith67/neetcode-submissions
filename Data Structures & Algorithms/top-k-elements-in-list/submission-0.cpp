class Solution {
public:
    static bool cmp(const pair<int, int> &a, const pair<int ,int> &b){
        return a.second > b.second;
    }

    vector<int> topKFrequent(vector<int>& nums, int k) {
        map<int, int> frequencyMap;

        for (auto num : nums) {
            frequencyMap[num]++;
        }

        vector<pair<int, int>> frequencyVector;

        // Fill frequencyVector with the entries from frequencyMap
        for (auto& entry : frequencyMap) {
            frequencyVector.push_back(entry);
        }

        // Sort by frequency in descending order
        sort(frequencyVector.begin(), frequencyVector.end(), cmp);

        vector<int> ans;
        for (int i = 0; i < k; i++) {
            ans.push_back(frequencyVector[i].first);  
        }

        return ans;
    }
};
