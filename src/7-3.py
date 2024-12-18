# 두 세트의 합집합
people = {"Jay", "Idrish", "Archil"}
vampires = {"Karan", "Arjun"}
dracula = {"Deepanshu", "Raju"}


# Union()을 사용하여 병합하기
population = people.union(vampires)
print("Union using union() function")
print(population)


# '|'를 사용하여 병합하기
population = people | dracula
print("\nUnion using '|' operator")
print(population)
