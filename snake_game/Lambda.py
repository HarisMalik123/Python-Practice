def myfunc(n):
    return lambda a: a*n


n=int(input("Enter Any Number "))
p=int (input("How many times you multiply it "))

number=myfunc(p)
print(number(n))