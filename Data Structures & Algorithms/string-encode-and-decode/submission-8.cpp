class Solution {
public:

    string encode(vector<string>& strs) {
        string res = "";
        for (string str: strs) {
            res += to_string(str.size()) + "#" + str;
        }
        return res;
    }

    vector<string> decode(string s) {
        vector<string> res;
        string len = "";
        for (int i = 0; i < s.size(); i++) {
            
            if (s[i] != '#') {
                len += s[i];
            } else {
                cout << len << endl;
                res.push_back(s.substr(i + 1, stoi(len)));
                cout << s.substr(i + 1, stoi(len)) << endl;
                i += stoi(len);
                len = "";
                
                
            }
        }
        return res;
    }
}; 
