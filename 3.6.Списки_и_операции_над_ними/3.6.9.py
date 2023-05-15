# put your python code here
name = input()
author = input()
pages = int(input())
price = float(input())

book = [name, author, pages, price]

del book[2]
book[1] = "Пушкин"
book[2] *= 2


print(book)