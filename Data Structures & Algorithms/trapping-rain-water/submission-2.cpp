class Solution {
public:
    int trap(vector<int>& height) {
        int l = 0;
        int r = height.size() - 1;
        int lmax = 0;
        int rmax = 0;
        int res = 0;

        while (l <= r) {
            int heightl = height[l];
            int heightr = height[r];

            if (heightl < heightr) {
                if (heightl > lmax) {
                    lmax = heightl;
                } else {
                    res += lmax - heightl;
                }
                l += 1;
            } else {
                if (heightr > rmax) {
                    rmax = heightr;
                } else {
                    res += rmax - heightr;
                }
                r -= 1;
            }
        }
        return res;

    }
};
