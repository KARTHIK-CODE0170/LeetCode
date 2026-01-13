/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    bool hasCycle(ListNode *head) {
        if(head == NULL)
            return false;
        ListNode *snail, *rabbit;
        snail = head;
        rabbit = head;
        while(rabbit != NULL && rabbit->next != NULL){
            snail = snail->next;
            rabbit = rabbit->next->next;
            if(snail == rabbit) return true;
                
        }

        return false;
        
    }
};