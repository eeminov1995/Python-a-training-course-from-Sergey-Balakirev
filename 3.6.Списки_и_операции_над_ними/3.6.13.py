# put your python code here
cities = ["Москва", "Тверь", "Вологда"]
cities_more = list(map(str, input().split()))
lst = cities + cities_more

print(*lst)