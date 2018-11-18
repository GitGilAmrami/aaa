MyString = '1243'
x = len(str(MyString)) + 1
step = None
start = 0
sum = 0

for start in range(x):
    stop = start + 1
    y = (MyString[start:stop:step])
    print("y: ",y)
    print(int(y))
    sum = sum + int(y)
    print (sum)
    start=start+1