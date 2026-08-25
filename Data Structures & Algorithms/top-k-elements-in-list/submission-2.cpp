class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> cnts;
        vector<vector<int>> freqs (nums.size() + 1);
        for (int num: nums) {
            cnts[num]++;
        }
        for (const auto& [num, cnt]: cnts) {
            freqs[cnt].push_back(num);
        }
        vector<int> res;
        for (int i = freqs.size() - 1; i >= 0; i--) {
            for (int num : freqs[i]) {
                res.push_back(num);
                if (res.size() == k) {
                    return res;
                }
            }
        }
    }
};
