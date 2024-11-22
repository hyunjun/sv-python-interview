class BIT:
    def __init__(self, n):
        self.n = n
        self.tree = [0] * (n + 1)

    def update(self, x, delta):
        while x <= self.n:
            self.tree[x] += delta
            x += x & -x

    def query(self, x):
        res = 0
        while x > 0:
            res += self.tree[x]
            x -= x & -x
        return res

    def dump(self):
        print("BIT status")
        print(*self.tree, sep=",")


class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        if not nums:
            return 0
        presum = 0
        values = set([0])
        """
        각 누적합에 대해 다음을 만족한다. 
        lower ≤ presum - x ≤ upper
        x ≤ presum - lower
        x ≤ presum - upper
        즉,
        presum – upper ≤ x ≤ presum - lower
        """
        for x in nums:
            presum += x
            values.add(presum)
            values.add(presum - lower)
            values.add(presum - upper)
        print(f"이전presum의 수치：{values}")
        # 희소하게 정렬된 값을 1~n으로 매핑
        x2i = {x: i + 1 for i, x in enumerate(sorted(set(values)))}

        # DEBUG 작업
        print("정렬된 추정값과 해당 위치를 출력한다.：")
        [print(key, value) for key, value in x2i.items()]
        bit = BIT(len(x2i))
        bit.update(x2i[0], 1)
        print("BIT에서 presum=0 값을 업데이트해야 한다.")
        bit.dump()
        res = cur = 0
        # 쌍으로 계산
        for i, x in enumerate(nums):
            cur += x
            print(f"배열의 {i}번째 요소 {x} 및 현재 접두어 합계 {cur}")
            # cursum 미만 - 상한
            print(f"cursum-upper={cur-upper} 인덱스 위치={x2i[cur - upper]}")
            l = bit.query(x2i[cur - upper] - 1)
            print(f"count of values < {cur - upper} {l}개 있음")
            # cursum보다 작거나 같음 – 더 낮음
            print(f"cursum–lower={cur-lower} 인덱스 위치={x2i[cur - lower]}")
            r = bit.query(x2i[cur - lower])
            print(f"count of values < {cur-lower} {r}개 있음음")
            res += r - l
            print(f"BIT의 현재 추정치={cur}에 해당하는 인덱스 {x2i[cur]}의 값을 업데이트해야 한다.")
            bit.update(x2i[cur], 1)
            bit.dump()
        return res
