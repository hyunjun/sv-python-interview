import collections


class Solution:
    def largestValsFromLabels(
        self, values: list[int], labels: list[int], num_wanted: int, use_limit: int
    ) -> int:
        # 값과 라벨을 묶고 가장 큰 값이 끝에 오도록 값을 오름차순으로 정렬한다.
        # 각 라벨이 사용된 횟수를 추적한다.
        options = sorted(zip(values, labels))

        # 카운터를 사용하여 각 라벨이 사용된 횟수를 추적한다.
        used_labels = collections.Counter()

        # 계속해서 가장 큰 값을 꺼낸다
        # (마지막 값이 항상 가장 크기 때문에 pop으로 가장 큰 값을 꺼낸다).
        # 라벨 사용횟수가 use_limit에 미치지 않으면,
        # res에 값을 추가하고 used_labels중 [label]칸에 1을 추가한다.
        # 모든 라벨을 다 사용했거나 num_wanted 값을 찾았으면
        # 계산을 중단하고 찾은 모든 값의 합계를 반환한다.
        res = []
        while (len(res) < num_wanted) and options:
            value, label = options.pop()
            if used_labels[label] < use_limit:
                used_labels[label] += 1
                res.append(value)

        return sum(res)
