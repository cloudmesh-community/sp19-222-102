def prime(n):
    for i in range (2, n-1):
        if((n%i)==0):
            break
    
    if(i<n):
        print("%d is a prime number" %(n))
        

prime(int(input("enter a number: ")))
            
