class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
    node, prev = head, None
    while node:
        # 다음 노드와 다음 노드와 현재 노드를 서로 바꾼 값을 저장한다.
        # 임시변수 next에 node.next를 넣어놓고, node.next에 prev를 넣는다.
        next, node.next = node.next, prev
        # prev에는 현재 노드로 업데이트하고, 현재 노드는 다음 노드로 업데이트한다.
        prev, node = node, next
    return prev
