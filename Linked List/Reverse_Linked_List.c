#include <stdio.h>
#include <stdlib.h>
/**
 * Definition for singly-linked list.
 */ 
struct ListNode {
    int val;
    struct ListNode *next;
};

struct ListNode* reverseList(struct ListNode* head){
    struct ListNode *prev, *cur, *next;
    if (head== NULL || head->next== NULL) {return head;}
    cur= next= head;
    prev= NULL;
    while (next!=NULL) {
        cur= next;
        next= cur->next;
        cur->next= prev;
        prev= cur;
    }
    return cur;
}
