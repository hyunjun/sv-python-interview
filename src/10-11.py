class BIT:
    def __init__(self, nums):
        self.tree = [0] * (len(nums) + 1)

    def sum_query(self, i):
        # 이진 인덱스 트리의 인덱스는 1부터 시작한다.
        output, i = 0, i + 1
        while i > 0:
            output += self.tree[i]
            i -= i & (-i)
        return output

    def update(self, i, delta=0):
        i += 1
        while 0 < i < len(self.tree):
            self.tree[i] += delta
            i += i & (-i)


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        # 숫자가 고유하고 정렬된 경우 숫자의 인덱스 위치를 확인하자.
        e2index = {e: i for i, e in enumerate(sorted(set(nums)))}
        bit = BIT(e2index)
        # 이 인덱스를 원래 순서로 다시 변환
        indexes = [e2index[e] for e in nums]
        # 이진 인덱스 트리에서 오른쪽에서 왼쪽 순회 발생 횟수
        output = []
        for index in indexes[::-1]:
            # 인덱스 왼쪽에 있는 모든 항목에 대한 합계
            output.append(bit.sum_query(index - 1))
            # 이 인덱스까지 발생 카운터 업데이트
            bit.update(index, 1)
        return output[::-1]
