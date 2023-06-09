# put your python code here
import math

marks = list(map(int, input().split()))

print(round(sum(marks) / len(marks), 1))