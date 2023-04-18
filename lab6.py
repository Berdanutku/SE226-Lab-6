import math

def equation1(n,a):
 f=lambda x,y:((x**i)/math.factorial(i))
 list=[]
 list.append(1)
 for i in range(1,n+1):
    list.append(f(a,i))
 print(sum(list))

n=int(input("Please enter 'n' number: "))
a=int(input("Please enter 'x' number: "))
equation1(n,a)

def equation2(n):
    """The function calculates and prints the result of the equation using a recursive function"""
    if n==0:
        return 0
    else:
        return ((((-1) ** (n + 1)) / n) + equation2(n - 1))


n=int(input("Please enter a number: "))
print(equation2(n))
print(equation2.__doc__)
