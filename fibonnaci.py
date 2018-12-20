def fibinit(n):
    if n==1:
        print(1)
    elif n==2:
        print("0\n1")
    else:
        print("0\n1")
        fibonnaci(n-2,0,1)
def fibonnaci(n,a,b):
    c=a+b
    a=b
    b=c
    print(c)
    if n>1:
        fibonnaci(n-1,a,b)

no=int(input("enter no. of digits\n"))
fibinit(no)
