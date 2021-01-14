def dox(num):
        return round((15 - 4*num)/5, 3)
def doy(num):
        return round((12 - 3*num)/7, 3)


x = float(input("initial value of x :"))
y = float(input("initial value of y :"))
n = int(input("Enter the no of iteration :"))
nos = 0
temp = x
while nos < n:
        print(f"{nos}      {dox(y)}      {doy(x)}")
        nos += 1
        x = dox(y)
        y = doy(temp)
        temp = x
        pass
