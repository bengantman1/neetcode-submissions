class Solution {
public:
    uint32_t reverseBits(uint32_t n) {

        uint32_t res = 0;
        int i = 0;
        while (n) {
            res |= (n & 1u) << (31 - i);
            n >>= 1;
            i++;
        }
        return res;

    }
};
