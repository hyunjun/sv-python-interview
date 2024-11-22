class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        a = set()

        while headA:
            a.add(headA)
            headA = headA.next

        while headB:
            if headB in a:
                return headB
            headB = headB.next

        return None
