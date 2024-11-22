class RandomizedSet:
    def __init__(self):
        # 데이터 구조 초기화
        self.data = []
        self.table = defaultdict()

    def insert(self, val: int) -> bool:
        # 해시테이블에 값을 삽입하고, 해시테이블에 지정된 원소가 이미 포함되어 있으면 True를 반환한다.
        if val in self.table:
            return False
        self.data.append(val)
        self.table[val] = len(self.data) - 1
        return True

    def remove(self, val: int) -> bool:
        # 해시테이블에서 값을 제거하고 해시테이블에 지정된 요소가 포함되어 있으면 True를 반환한다.
        # 마지막 원소와 교환하는 데 사용되는 삭제된 원소의 인덱스를 가져온다.
        removed_idx, last_idx = self.table[val], len(self.data) - 1
        item = self.data[last_idx]

        # 마지막 원소의 위치 업데이트
        self.table[item] = removed_idx

        # 삭제할 원소와 마지막 원소를 교체한다.
        self.data[removed_idx], self.data[last_idx] = self.data[last_idx], val

        # 삭제
        self.data.pop()
        del self.table[val]
        return True

    def getRandom(self) -> int:
        # 난수 생성 및 인덱스 생성
        idx = random.randint(0, len(self.data) - 1)
        return self.data[idx]
