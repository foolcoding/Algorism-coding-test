import sys
import math

n = int(sys.stdin.readline())
print(math.ceil((3 + math.sqrt(12 * n - 3)) / 6))