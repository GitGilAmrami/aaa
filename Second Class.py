### Second Class ###

#A .

X = 4
Y = 6

if X < Y:
    print(" SMALL ")
elif X > Y:
    print(" BIGER ")

#B.

for x in range(5):
    print(x)

#C.
season = 4

if season == 1:
    print ('summer')
elif season == 2:
    print ('winter')
elif season == 3:
    print ('fall')
elif season == 4:
    print ('spring')

#D.

count=1
while count < 11:
    print(count)
    count+=1
##10 times
## 1 2 3 4 5 6 7 8 9 10

#E.

MyAge=99
Family='A'
currency=3.5
abroad='YES'
apartmentNum=8

print (MyAge,Family,currency,abroad,apartmentNum)
print(currency+MyAge)


#F.

Phone = input ("Please enter your phone number ...")
print ("phone number: " + Phone)


#G.

class myclass:

    def printHello(self ):
        print('hello')

    def calculate(self ):
        print( 5+3.2 )

if __name__ == '__main__':
    myclass().printHello()
    myclass().calculate()

#H.

class main2:

    def printName(self, mname):
        print (mname)

    def DevideNumber(self,mnumber):
        print(mnumber/2)

if __name__ == '__main__':
    mname = input ("Please enter your name ...")
    mnumber = int(input ("Please enter your number ..."))

    main2().printName(mname)
    main2().DevideNumber(mnumber)

#I.
class main3:
    def return_sum(sel, x, y):
        return (x + y)

    def return_string(self, string1, string2):
        return (string1  + string2)


if __name__ == '__main__':
    string1 = 'BE'
    string2 = 'GOOD'
    y = 5
    x = 6

    sumNumber = main3().return_sum(x, y)
    print(sumNumber)
    strAll = main3().return_string(string1, string2)
    print(strAll)


#K.

Mystring = 'X'

for i in range(0, 5):

    print(Mystring)
    Mystring = "X" + Mystring


#L.

N = 7

for i in range(N):
    for j in range(N):
        if (i == j) or ((N - j - 1) == i):
            print('*', end = '')
        else:
            print(' ', end = '')
    print('')

#M. ERROR

MyString = '1243'
x = len(str(MyString)) + 1
step = None
start = 0
sum = 0

for start in range(x):
    stop = start + 1
    y = (MyString[start:stop:step])
    sum = sum + int(y)
    print (sum)
    start=start+1