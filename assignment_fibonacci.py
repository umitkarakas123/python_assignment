n = int(input("Enter is a number: "))
fib1 = [0]
fib2 = [0,1] 
if n <= 0 : 
    print("This is Wrong") 
elif n == 1 :
    print(fib1)
elif n > 1 and  n <= 2: 
    print(fib2) 
else:
    for i in range(2,n):
        total = fib2[i-1] + fib2[i-2] 
        fib2.append(total) 
    print(fib2) 
  