class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_set<int> my_set (nums.begin(), nums.end());
        cout << nums.size() << endl;
        cout << my_set.size() << endl;
        return my_set.size() != nums.size();
    }
};