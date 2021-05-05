number = input("Enter a positive number: ")
if number.isdecimal() == False or type(number) == float or int(number) <= 1 :
    print("It is an invalid entry. Don't use non-numeric, float, or negative values!")
elif int(number) > 1 :
    i = int(number)
    for x in range(2, i) :
        if (i % x == 0) :
            print(f"The number {number} is not a prime number")
            break
    else :
        
        print(f"The number {number} is a prime number")
        