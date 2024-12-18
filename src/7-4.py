# 두 집합의 교집합
set1 = set()
set2 = set()
for i in range(5):
    set1.add(i)
for i in range(3, 9):
    set2.add(i)

# intersection()을 사용하여 교집합 구하기
set3 = set1.intersection(set2)
print("Intersection using intersection() function")
print(set3)

# '&'를 사용하여 교집합 구하기
set3 = set1 & set2
print("\nIntersection using '&' operator")
print(set3)
