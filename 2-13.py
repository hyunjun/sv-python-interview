def find_pivot(nums):
    m = nums[-1]
    i = len(nums) - 1
    while i >= 0 and nums[i] >= m:
        m = nums[i]
        i -= 1
    return i


def find_successor(nums, pivot):
    j = len(nums) - 1
    while nums[pivot] >= nums[j]:
        j -= 1
    assert j > pivot
    return j


def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        if len(nums) < 2:
            return
        # 첫 번째 내림차순 인덱스 찾기
        i = find_pivot(nums)
        if i < 0:
            nums.sort()
        else:
            # nums[i]보다 작은 i를 찾으면 교환할 값인 j를 찾는다.
            j = find_successor(nums, i)
            # 인덱스 위치 i와 j의 숫자를 바꾼다.
            nums[i], nums[j] = nums[j], nums[i]
            # 인덱스 위치 이후 배열 정렬
            reverse(nums, i + 1, len(nums) - 1)

        # 첫 번째 내림차순 인덱스 찾기
        i = find_pivot(nums)
        if i < 0:
            nums.sort()
        else:
            # i 다음에 nums[i]보다 작은 내림차순 첫 번째 인덱스 j를 찾는다.
            j = find_successor(nums, i)
            # 인덱스 위치 i와 j의 숫자를 교환한다.
            nums[i], nums[j] = nums[j], nums[i]
            # 인덱스 위치 i 이후 배열 정렬
            reverse(nums, i + 1, len(nums) - 1)
