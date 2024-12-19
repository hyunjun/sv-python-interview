class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def fn(node):  # 문자열을 숫자로 변환하는 함수 정의
            """연결 리스트를 표시하는 반환 숫자"""
            ans = 0
            while node:
                ans = 10 * ans + node.val
                node = node.next
            return ans

        # dummy 노드 정의
        dummy = node = ListNode()
        for i in str(fn(l1) + fn(l2)):
            node.next = ListNode(int(i))  # 지속적으로 각 값을 노드로 가져온다.
            node = node.next  # 다음 노드로 이동
        return dummy.next
