L=["(*,×),(+),(-),(/,÷),(**,^),(%),(!),(sqrt,√),(sq,²),(cub,³),(cubrt,³√)(nth root<nrt>),df,df2"]
while True:
    print("")
    print('available operators are:',L)
    print("")
    print("Please enter operand 1")
    x=float(input("Enter : "))
    print("")
    print("Please enter operand 2(if  any, else enter 0)")
    y=float(input("Enter : "))
    print("")
    print("select your operator")
    print("")
    z=input("Enter: ").lower()
    if z in 'df2':
        y=int(input("Enter the maximum denominator value: "))
    n=1
    if z in ['*','×','x']:
        print("result: ",x*y)
    elif z=='+':
        print("result: ",x+y)
    elif z=='-':
        print("result: ",x-y)
    elif z in ['/','÷']:
        if y==0:
             print("invalid")
        else:
            print("result: ",x/y)
    elif z in ['**','^']:
         import math
         if x==0:
             print ("result: ",0)         
         else:
          n=(y*(math.log(x))+1)
          n.is_integer()
          if n<308:     
           print("result: ",x**y)
          else:
             print("result too large to display ")
    elif z=='%':
        print("result: ",x%y)
    elif z=='!':
       if x>=171:
           print("number is too large for factorial calculation,try again")
       elif x.is_integer() and x>-1:
         while x>=2:
                n=(n)*(x)*(x-1)
                x=x-2
         print("result: ",n)
       else:
            print("invalid")
    elif z in ['sqrt','√']:
        if x>=0:
         n=x**(1/2)
         print("result is: ",n)
        if x<0:
            print("invalid for sqrt")
    elif z in ['cubrt','³√']:
        if x>0:
            n=x**(1/3)
        else:
            n=-((-x)**(1/3))
        print("result is: ",n)
    elif z in ['sq','²']:
        n=x**2
        print("result is: ",n)
    elif z in ['cube','³']:
        n=x**3
        print('result is: ',n)
    elif z in ['nth root','nrt']:
        if y==0:
            print("invalid")
        else:
            n=x**(1/y)
            print("result is: ",n)
    elif z in ['decimal to fraction','df']:
        from fractions import Fraction
        print("result is: ",Fraction(x).limit_denominator())
    elif z in ['decimal to fraction2','df2']:
            from fractions import Fraction
            print("result is: ",Fraction(x).limit_denominator(y))
    else:
        print("retry")