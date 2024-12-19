class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        def size(head: ListNode):
            n = 0
            while head:
                n += 1
                head = head.next
            return n

        # 각 연결 리스트의 노드 수를 구한다.
        nA = size(headA)
        nB = size(headB)

        if nA == 0 or nB == 0:
            return None

        itr1 = headA
        itr2 = headB

        # 연결 리스트 노드 수의 차를 구한다.
        d = nA - nB
        if d > 0:
            while d > 0:
                itr1 = itr1.next
                d -= 1
        else:
            while d < 0:
                itr2 = itr2.next
                d += 1

        # 현재 두 연결 리스트의 길이가 동일하므로 순회를 시작한다.
        while itr1 != itr2:
            itr1 = itr1.next
            itr2 = itr2.next

        return itr1
