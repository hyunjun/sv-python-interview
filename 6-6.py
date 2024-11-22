# 딕셔너리 초기화
Dict = {
    5: "Welcome",
    6: "To",
    7: "Geeks",
    "A": {1: "Geeks", 2: "For", 3: "Geeks"},
    "B": {1: "Geeks", 2: "Life"},
}
print("Initial Dictionary: ")
print(Dict)

# 딕셔너리에서 del을 사용하여 원소 삭제
del Dict[6]
print("\nDeleting a specific key: ")
print(Dict)

# 삽입된 ‘값’ 삭제
del Dict["A"][2]
print("\nDeleting a key from Nested Dictionary: ")
print(Dict)
