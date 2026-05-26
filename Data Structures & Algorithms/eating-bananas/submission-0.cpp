class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) {
        int s = 1;
        int e = *max_element(piles.begin(), piles.end());
        int result = e;

        while(s <= e) {
            int k = s + (e - s)/2;
            long long totalHours = 0;
            for(auto pile : piles) {
                totalHours += (pile + k - 1) / k;
            }
            if(totalHours <= h){
                result = k;
                e = k - 1; //still a better soln might be found
            }
            else {
                s = k + 1;
            }
        }

        return result;
    }
};