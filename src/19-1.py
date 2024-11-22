from collections import deque


class Entity:
    def __init__(self, id, type, name, size, children):
        self.id = id
        self.type = type
        self.name = name
        self.size = size
        self.children = children


class FileSystem:
    def __init__(self):
        self.id_to_entity = self.build_dict()

    def entity_size(self, entity_id: int) -> int:
        # 엔터티_id와 연관된 파일 또는 디렉터리의 크기를 반환한다.
        if entity_id not in self.id_to_entity:
            return -1
        # 딕셔너리를 사용하여 엔터티 ID와 연관된 엔터티를 찾는다.
        entity = self.id_to_entity[entity_id]
        # 현재 엔터티가 디렉터리이면 재귀를 계속한다.
        if entity.type == "directory":
            return self.dfs(entity)
        # 현재 엔터티가 파일이면 파일 크기를 반환한다.
        if entity.type == "file":
            return entity.size

        return 0

    def build_dict(self):
        # 딕셔너리 선언
        entities = [
            Entity(id=1, type="directory", name="root",
                   size=0, children=[2, 3]),
            Entity(id=2, type="directory", name="dir",
                   size=0, children=[4, 5]),
            Entity(id=3, type="file", name="file1", size=100, children=[]),
            Entity(id=4, type="file", name="file2", size=200, children=[]),
            Entity(id=5, type="file", name="file3", size=300, children=[]),
        ]
        Dict = {}
        for entity in entities:
            Dict[entity.id] = entity
        return Dict

    def dfs(self, entity):
        if entity.type == "file":
            return entity.size
        if entity.type == "directory" and len(entity.children) == 0:
            return 0
        # dfs 함수 사용(코드에서는 생략)
        res = 0
        for child in entity.children:
            res += self.dfs(self.id_to_entity[child])
        return res
