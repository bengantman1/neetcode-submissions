class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        
        unordered_map<string, vector<string>> dict;
        vector<vector<string>> res;
        
        
        for(string str: strs) {
            string new_str = str;
            sort(new_str.begin(), new_str.end());
            dict[new_str].push_back(str);
        } 
        for (const auto& [key, value] : dict) {
            res.push_back(value);
        }
        return res;
    }
};
