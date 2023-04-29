# put your python code here
a, b, c = map(int, input().split())

print(a + b > c and b + c > a and c + a > b)