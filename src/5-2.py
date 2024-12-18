import heapq

customers = []
heapq.heappush(customers, (2, "Harry"))
heapq.heappush(customers, (3, "Charles"))
heapq.heappush(customers, (1, "Riya"))
heapq.heappush(customers, (4, "Stacy"))
while customers:
    # Riya, Harry, Charles, Stacy 순으로 출력한다.
    print(heapq.heappop(customers))