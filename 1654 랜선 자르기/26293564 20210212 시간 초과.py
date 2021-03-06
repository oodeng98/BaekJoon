def find_best(start, finish, lst, need):
    while True:
        if finish - start <= 1:  # 1?
            break
        middle = (start + finish) // 2
        check = 0
        for i in lst:
            check += i // middle
        if check >= need:
            start = middle
        else:
            finish = middle
    return start


nums = input().split(' ')
num = int(nums[0])
need = int(nums[1])
data = []
for i in range(num):
    d = int(input())
    data.append(d)

total = 0
for i in data:
    total += i
best = total / need

print(int(find_best(1, best, data, need)))
