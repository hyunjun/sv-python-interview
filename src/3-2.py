from collections import deque

stack = deque()

# append() 함수로 스택의 가장 위에 원소를 추가한다.
stack.append("a")
stack.append("b")
stack.append("c")
print("Initial stack:")
print(stack)

# pop() 함수로 스택에서 LIFO 순서로 원소를 추출한다.
print("\nElements popped from stack:")
print(stack.pop())
print(stack.pop())
print(stack.pop())
print("\nStack after elements are popped:")
print(stack)
