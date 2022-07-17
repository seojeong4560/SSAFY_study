T = int(input())
numbers = list(map(int, input().split()))

for tc in range(1, T + 1):
    for i in range(T - 1):
        for j in range(T - 1 - i):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

mid_index_number = int(T / 2)
mid_number = numbers[mid_index_number]

print("{}".format(mid_number))
