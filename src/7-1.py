# 세트에 원소를 추가한다.
# 세트 생성
people = {"Jay", "Idrish", "Archi"}
print("People:", end=" ")
print(people)

# 세트에 Daxit 추가
people.add("Daxit")

# 반복문을 사용하여 세트에 원소를 추가한다.
for i in range(1, 6):
    people.add(i)
print("\nSet after adding element:", end=" ")
print(people)
