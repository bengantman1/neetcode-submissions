class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> dict; // {number: index}
        for (int i = 0; i < nums.size(); i++) {
            int need = target - nums[i];
            if (dict.find(need) != dict.end()) {
                vector<int> res = {dict[need], i};
                return res;
            } else {
                dict[nums[i]] = i;
            }
            
        }
        return {0,0};
    }
};
