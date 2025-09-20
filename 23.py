# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional
class Solution:
    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        result_head = ListNode(-1, None)
        runner = result_head
        while any(lists):
            min_val = float('inf')
            min_val_idx = 0
            for idx, l in enumerate(lists):
                if l and l.val <= min_val:
                    min_val = l.val
                    min_val_idx = idx
            runner.next = ListNode(min_val, None)
            runner = runner.next
            lists[min_val_idx] = lists[min_val_idx].next
        return result_head.next
