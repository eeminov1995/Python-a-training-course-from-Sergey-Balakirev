# put your python code here
lst = list(map(int, input().split()))
last_element = lst.pop()
lst.append(last_element % 2 != 0)


print(*lst)