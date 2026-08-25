class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()) return false;
        unordered_map<char, int> freqs;
        for (char c : s) {
            if (freqs.find(c) != freqs.end()) {
                freqs[c] += 1;
            } else {
                freqs[c] = 1;
            }
        }

        for (char c : t) {
            if ((freqs.find(c) == freqs.end()) || freqs[c] == 0) {
                return false;
            }
            freqs[c]--;
        }
        return true;
    }
};
