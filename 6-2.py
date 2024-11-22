# 빈 딕셔너리 만들기
Dict = {}
print("Empty Dictionary: ")
print(Dict)

# dict() 메서드를 사용하여 딕셔너리를 만들기
Dict = dict({1: "Geeks", 2: "For", 3: "Geeks"})
print("\nDictionary with the use of dict(): ")
print(Dict)

# 각 항목이 쌍으로 다루어지는 딕셔너리를 만든다.
Dict = dict([(1, "Geeks"), (2, "For")])
print("\nDictionary with each item as a pair: ")
print(Dict)
