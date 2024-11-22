def countRangeSum_bs(self, nums, lower, upper):
    import bisect

    count, s = 0, 0
    sorted_sums = [0]
    for x in nums:
        s += x  # sum[i+1]를 표시한다.
        l = bisect.bisect_left(sorted_sums, s - upper)
        r = bisect.bisect_right(sorted_sums, s - lower)
        count += r - l
        bisect.insort(sorted_sums, s)
    return count
