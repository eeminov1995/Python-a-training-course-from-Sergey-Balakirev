# put your python code here
w1, w2 = map(str, input().split())

w1_1 = w1[1:len(w2):2]
w2_2 = w2[1::2]

print(w1_1 == w2_2)