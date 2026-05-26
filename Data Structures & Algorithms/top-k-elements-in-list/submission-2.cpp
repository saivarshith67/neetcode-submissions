class Solution {
public:

    //nlogn time
    // static bool cmp(const pair<int, int> &a, const pair<int ,int> &b){
    //     return a.second > b.second;
    // }

    // vector<int> topKFrequent(vector<int>& nums, int k) {
    //     map<int, int> frequencyMap;

    //     for (auto num : nums) {
    //         frequencyMap[num]++;
    //     }

    //     vector<pair<int, int>> frequencyVector;

    //     for (auto& entry : frequencyMap) {
    //         frequencyVector.push_back(entry);
    //     }

    //     sort(frequencyVector.begin(), frequencyVector.end(), cmp);

    //     vector<int> ans;
    //     for (int i = 0; i < k; i++) {
    //         ans.push_back(frequencyVector[i].first);  
    //     }

    //     return ans;
    // }


    //O(n) time and O(n) space
    vector<int> topKFrequent(vector<int>& nums, int k) {
        // IDEA : we use bucket sort.
        /*
        so here the ith index represents frequency of an element and a list of 
        elements that has that frequency for example
        input : nums = [1,2,2,3,3,3], k = 2
        map : {
            1 : [1] -> value is the list of elements that has frequency as 1
            2 : [2]
            3 : [3]
        }
        */

        map<int, int> countMap;

        // number : frequency
        for(int num : nums){
            countMap[num]++;
        }

        vector<vector<int>> frequency(nums.size() + 1);

        for(auto pair : countMap) {
            frequency[pair.second].push_back(pair.first);
        }

        // Collect the top k frequent elements
        vector<int> result;
        for (int i = frequency.size() - 1; i >= 0 && result.size() < k; i--) {
            if (!frequency[i].empty()) {
                for (int num : frequency[i]) {
                    result.push_back(num);
                    if (result.size() == k) break;
                }
            }
        }

        return result;

    }
};
