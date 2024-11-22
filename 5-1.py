customers = []
customers.append((2, "Harry"))
customers.append((3, "Charles"))
customers.sort(reverse=True)

# 우선순위를 유지하려면 정렬이 필요하다.
customers.append((1, "Riya"))
customers.sort(reverse=True)
# 우선순위를 유지하려면 정렬이 필요하다.
customers.append((4, "Stacy"))
customers.sort(reverse=True)
while customers:
    print(customers.pop(0))
    # 해당 순서대로 이름을 출력한다: Stacy, Charles, Harry, Riya.
