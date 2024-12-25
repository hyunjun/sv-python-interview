class Solution:
    def numBusesToDestination(self, routes: list[list[int]], S: int, T: int) -> int:
        if S == T:
            return 0
        stop_bus = collections.defaultdict(list)
        # 각 정류장에 해당하는 버스 노선을 저장하는 데 사용된다.
        for i, route in enumerate(routes):
            for stop in route:
                stop_bus[stop].append(i)

        # BFS를 위한 큐 데이터 구조 정의
        bus_visited = set()
        queue = collections.deque()
        queue.append((S, 1))

        while queue:
            # 현재 정류장에서 갈 수 있는 버스 노선을 확인한다.
            stop, buses = queue.popleft()
            # 모든 버스 노선 감지
            for bus in stop_bus[stop]:
                # 해당 버스 정류장을 이미 통과했다면 지나간다.
                if bus in bus_visited:
                    continue
                bus_visited.add(bus)
                # 해당 버스 노선의 모든 정류장이 T인지 확인한다.
                for s in routes[bus]:
                    if s == T:
                        return buses
                    queue.append((s, buses + 1))
        return -1
