# recursion
 #factorial number

#def factorial(n):
 #   if n==0:
  #      return 1
   # else:
    #    a=n*factorial(n-1)
     #   return a
#n=int(input('enter num='))  #input from user
#res=factorial(5)
#print(res)

#fibonacci series

def fib(n):
    if n==0: 
        return 1
    if n==1:
        return 1
    
    else:
        a=fib(n-1)+fib(n-2)
        return a
b=fib(8)
print(b)



    
