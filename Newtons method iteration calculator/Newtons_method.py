# python function to find the recursion of our first sum in Newton`s Method
# for each problem please change the recrusive algorithm
import math
boo = True
while boo:
    c = int(input("enter 1 to continue or 0 to stop"))
    if c == 0 :
        boo = False
        break
    val = float(input("enter the mid value:"))
    n = int(input("enetr the range:"))
    for i in range(n):
        res = 3/(val - 2)
        print(res)
        val = res
        print(i)

