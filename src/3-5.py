class Node:
    def __init__(self, id: int, time_flag: str, time_stamp: int):
        self.id = id
        self.time_flag = time_flag
        self.time_stamp = time_stamp


class Solution:
    def exclusiveTime(self, n: int, logs: list[str]) -> list[int]:
        nodes = []
        stk = []
        res = [0] * n

        for log in logs:
            # 로그 분석
            parse_log = log.split(":")
            nodes.append(
                Node(int(parse_log[0]), parse_log[1], int(parse_log[2])))

        for node in nodes:
            if node.time_flag == "start":
                stk.append(node)  # 스택에 추가
            else:
                time_duration = node.time_stamp - stk[-1].time_stamp + 1
                res[node.id] += time_duration
                stk.pop()  # 스택에서 팝

                if stk:
                    # 이전 함수에 현재 종료된 함수 실행시간을 뺀다.
                    res[stk[-1].id] -= time_duration

        return res


if __name__ == "__main__":
    exclusive = Solution()
    logs = ["0:start:0", "1:start:2", "1:end:5", "0:end:6"]
    n = 2
    res = exclusive.exclusiveTime(n, logs)
    print(res)
