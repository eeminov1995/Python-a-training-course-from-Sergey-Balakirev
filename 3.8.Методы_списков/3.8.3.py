# put your python code here
lst = list(map(int, input().split()))
lst.append(lst[0] != lst[-1])

print(*lst)