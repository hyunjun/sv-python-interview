class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if numCourses == 0:
            return true

        # indegree = 0인 노드 찾기, 해당 과목은 선행과목 없이 먼저 수강할 수 있다.
        # 완료 후, 해제할 수 있는 각 preReq의 필수과목을 기록한다. Node -> leafs
        adj = [[] for _ in range(numCourses)]
        q = deque()

        # 각 과목에 필요한 선행강좌 수를 기록한다.
        indegree = [0] * numCourses
        count = 0

        for i in range(len(prerequisites)):
            # 전과정 이수 후 사후과정 수강 가능
            adj[prerequisites[i][1]].append(prerequisites[i][0])
            # indegree 기록, 과정의 선행 조건 번호 + 1,
            indegree[prerequisites[i][0]] += 1

        # indegree가 0이고 선행과목이 필요하지 않은 과목을 찾아서 큐에 넣는다.
        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)
                count += 1

        # indegree = 0인 과정을 탐색하여 다른 과정이 모두 수강 가능할때까지 진행하고 True를 반환한다.
        while q:
            # 현재 강좌를 수강한 후 현재는 후행 강좌의 잠금을 해제한다.
            front = q.popleft()
            for child in adj[front]:
                indegree[child] -= 1
                # 차수가 0인 새 클래스가 생성되면 이를 q에 넣는다.
                if indegree[child] == 0:
                    q.append(child)
                    count += 1

        return count == numCourses
