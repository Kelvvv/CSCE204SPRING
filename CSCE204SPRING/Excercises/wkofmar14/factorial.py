def factorial(num): #num becomes 7
    answer = 1

    if num < 0:
        print("Invalid number")
        return

    for i in range(1, num + 1):
        answer *= i

    return answer

result = factorial(7)
print(f"7! = {result}")