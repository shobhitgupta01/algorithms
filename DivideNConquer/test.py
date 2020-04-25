import datetime
i = 2
a = datetime.datetime.now()
i = i * 2
b = datetime.datetime.now()
print(b-a)
print("The time taken for multiplication is {}".format(b-a))

j = 3
a = datetime.datetime.now()
j = j << 2
b = datetime.datetime.now()
print("The time taken for left shift is {}".format(b-a))