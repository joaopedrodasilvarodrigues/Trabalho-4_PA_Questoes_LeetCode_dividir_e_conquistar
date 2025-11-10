/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
#include <stdlib.h>
struct ListNode* mergePar(struct ListNode* a, struct ListNode* b);

struct ListNode* mergeKLists(struct ListNode** lists, int listsSize) {
    if (listsSize ==0) return NULL;
    while (listsSize >1) {
        int newSize =0;
        for (int i =0; i < listsSize; i +=2) {
         if (i+1 <listsSize)
            lists[newSize++] = mergePar(lists[i], lists[i+1]);
          else
             lists[newSize++] = lists[i];
        }
        listsSize = newSize;
    }

    return lists[0];
}

struct ListNode* mergePar(struct ListNode* a, struct ListNode* b) {
    if (!a) return b;
    if (!b) return a;
    if (a->val <b->val) {
        a->next = mergePar(a->next, b);
        return a;
    } else {
        b->next = mergePar(a, b->next);
        return b;
    }
}
