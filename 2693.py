n = int(input())
array = [[0 for _ in range(10)] for _ in range(n)]

for i in range(n):
    a = list(map(int, input().split()))
    array[i] = a

for i in range(n):
    array[i].sort()

for i in range(n):
    print(array[i][7])