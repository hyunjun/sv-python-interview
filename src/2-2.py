# 리스트에 원소 추가
# 리스트를 초기화한다.
List = []
print("Initial blank List: ")
print(List)

# 리스트에 원소 추가
List.append(1)
List.append(2)
List.append(4)
print("\nList after Addition of Three elements: ")
print(List)

# 반복문을 사용하여 리스트에 원소를 추가한다.
for i in range(1, 4):
 List.append(i)
print("\nList after Addition of elements from 1-3: ")
print(List)

# 리스트에 튜플 추가.
List.append((5, 6))
print("\nList after Addition of a Tuple: ")
print(List)

# 리스트에 리스트 추가
List2 = ["For", "Geeks"]
List.append(List2)
print("\nList after Addition of a List: ")
print(List)
