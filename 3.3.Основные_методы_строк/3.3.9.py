# put your python code here
n1, n2, n3 = map(int, input().split())

print(str(n1).rjust(3, '0'), str(n2).rjust(3, '0'), str(n3).rjust(3, '0'), sep='\n')