leap = int(input("Enter is number: "))
if (leap % 4 == 0) :
    if leap % 400 == 0 :
        print(f"{leap} is a leap year")
    elif (leap % 100 == 0) :
        print(f" {leap} is not a leap year")
    else:   
        print(f"{leap} is a leap year")
else:
        print(f"{leap} is not a leap year")
