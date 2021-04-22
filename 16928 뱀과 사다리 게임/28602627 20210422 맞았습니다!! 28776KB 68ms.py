import sys

input = sys.stdin.readline
n, m = map(int, input().split())
ladder_snake = {}
snake_ladder = {}
for i in range(n + m):
    key, value = map(int, input().split())
    ladder_snake[key] = value
    snake_ladder[value] = key
climb_from_start = set(ladder_snake.keys())
climb_from_end = set(snake_ladder.keys())
start = {1}
end = {100}
count = 0
while True:
    count += 1
    from_start = set()
    for i in start:
        for j in range(1, 7):
            from_start.add(i + j)
    common = from_start & climb_from_start
    for i in common:
        from_start.add(ladder_snake[i])
    if from_start & end:
        break
    start = from_start - common
print(count)
