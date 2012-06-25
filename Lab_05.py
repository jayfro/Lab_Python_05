def fact(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return x * fact(x-1)

'''for x in range(0,10):

    print '%d! = %d' %(x, fact(x)) '''


#problem 2



def factorial(n):

    
          if (n == 0):
              
              return 1
            
          else:

              
              return n * factorial(n - 1)

fact = input ("enter number")

#print factorial (5)   #when it is pre defined!!!!

print factorial (fact)  #not predefined



'''#problem 3
            
# compute the nth Fibonacci number
# n must be non-negative!
    
def fibonacci(n):
        if (n == 0):
            return 0
        elif (n == 1):
            return 1
        else:
            return fibonacci(n-1) + fibonacci(n-2)'''




#problem 4 prime (true/false)


def isprime(startnumber):
    startnumber*=1.0
    for divisor in range(2,int(startnumber**0.5)+1):
        if startnumber/divisor==int(startnumber/divisor):
            return False
    return True

   
prime = input("enter number")

print isprime(prime)

               

#challage problems

#problem 4



def is_palindrome(s):
    b=True
    for i in range(len(s)/2):
        if s[i]!=s[-i-1]:
            b=False
    return b
s=raw_input("Enter palindrome: ")
print is_palindrome(s)


