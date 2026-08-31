/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* cur = head;
        int len = 0;
        while (cur != nullptr) {
            len++;
            cur = cur->next;
        }
        
        int targetIdx = len - n;
        if (targetIdx == 0) {
            ListNode* del = head;
            head = head->next;
            delete del;
            return head;
        }
        ListNode* prev = nullptr;
        cur = head;
        while (targetIdx > 0) {
            prev = cur;
            cur = cur->next;
            targetIdx -= 1;
        }
        prev->next = cur->next;
        delete cur;

        return head;
    }
};
