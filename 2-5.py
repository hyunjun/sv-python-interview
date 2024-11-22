# 리스트에서 원소를 삭제하기 위해 먼저 리스트를 만든다.
List = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
print("Intial List: ")
print(List)

# 리스트에서 원소를 제거한다.
# remove() 함수를 사용한다.
List.remove(5)
List.remove(6)
print("\nList after Removal of two elements: ")
print(List)

# 리스트에서 원소를 제거한다.
# 반복문을 사용한다
for i in range(1, 5):
    List.remove(i)
print("\nList after Removing a range of elements: ")
print(List)
