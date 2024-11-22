# 빈 딕셔너리 만들기
Dict = {}
print("Empty Dictionary: ")
print(Dict)

# 딕셔너리에 원소를 추가한다.
Dict[0] = "Geeks"
Dict[2] = "For"
Dict[3] = 1
print("\nDictionary after adding 3 elements: ")
print(Dict)

# 딕셔너리에 원소 세트 추가
Dict["Value_set"] = 2, 3, 4
print("\nDictionary after adding 3 elements: ")
print(Dict)

# 딕셔너리의 키 값을 업데이트한다.
Dict[2] = "Welcome"
print("\nUpdated key value: ")
print(Dict)

# 내장된 딕셔너리를 딕셔너리의 키 값에 추가한다.
Dict[5] = {"Nested": {"1": "Life", "2": "Geeks"}}
print("\nAdding a Nested Key: ")
print(Dict)
