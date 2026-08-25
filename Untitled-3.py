print("hello human")
print("this is a program that will calculate the quadratic equation and tell you the roots of the equation")
a=int(input("enter the value of a:"))
if a==0:
    print("the value of a cannot be zero")
    
else:
    b=float(input("enter the value of b:"))
    c=float(input("enter the value of c:"))

    d= (-b+((b**2-4*a*c)**0.5))/(2*a)
    e= (-b-((b**2-4*a*c)**0.5))/(2*a)
    print("the roots of the equation are",(d),"and",(e))

