def funx(y, z):
    return round((3 + 5*y + 2*z)/10, 3)
def funy(x, z):
    return round(((3 + 4*x + 3*z)/10), 3)
def funz(x, y):
    return round(((- 3 - x - 6*y)/10), 3)

x = float(input("Enter the value of x :"))
y = float(input("Enter the value of y :"))
z = float(input("Enter the value of z :"))
n = int(input("Enter the number of Iteration :"))
nos = 0
while nos <= n:
    print(f"{nos} {funx(y, z)}   {funy(x, z)}  {funz(x, y)}")
    temp1 = x
    temp2 = y
    temp3 = z
    x = funx(y, z)
    y = funy(temp1, z)
    z = funz(temp1, temp2)
    nos += 1
