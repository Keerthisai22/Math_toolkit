def square(n):
    return n*n
def cube(n):
    return n*n*n
def fact(n):
    if n==1 or n==0:
        return 1
    return n*fact(n-1)
