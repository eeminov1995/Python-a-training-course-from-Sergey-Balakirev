import math
# ввод данных
n, k = map(int, input().split())

# здесь продолжите программу
print(math.trunc(math.factorial(n) / (math.factorial(k) * math.factorial(n - k))))
