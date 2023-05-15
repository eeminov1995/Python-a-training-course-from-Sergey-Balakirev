# put your python code here
nums = list(map(int, input().split()))
nums.sort()

print(*nums[:3])