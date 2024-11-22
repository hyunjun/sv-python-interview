def countSmaller_bs(self, nums):
    """
    처음부터 끝까지 반복하고 정렬된 목록을 유지한다. 각 루프에 대해 현재 숫자를 정렬된 목록에 넣고 삽입 위치를 기록한다.  

    """

    res = []
    sorted = []
    from bisect import bisect_left
    for i in reversed(range(len(nums))):
        idx = bisect_left(sorted, nums[i])
        sorted.insert(idx, nums[i])
        res.append(idx)
    res.reverse()
    return res
