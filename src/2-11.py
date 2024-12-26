class Solution:
    def __init__(self, nums: list[int]):
        # 각 원소의 인덱스 위치를 저장하는 해시 테이블을 만든다.
        self.nums = collections.defaultdict(list)
        for indx, ele in enumerate(nums):  # 리스트 탐색
            self.nums[ele].append(indx)  # 각 원소에 대해 해당 인덱스 위치를 추가한다.

    def pick(self, target: int) -> int:
        # Python 함수 random.choice()를 호출한다.
        return random.choice(self.nums[target])
