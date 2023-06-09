# put your python code here
name, patronymic, surname = map(str, input().split())

print(f'{surname} {name[:1]}.{patronymic[:1]}.')
