# put your python code here
rivers = list(map(str, input().split()))

rivers.sort()
rivers.remove(rivers[0])

print(*rivers)
