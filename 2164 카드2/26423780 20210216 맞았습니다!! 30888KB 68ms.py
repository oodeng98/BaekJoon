import sys
import math
input = sys.stdin.readline

num = int(input())
if num == 1 or num == 2:
    print(num)
else:
    print((num - 2 ** int(math.log(num-1, 2))) * 2)