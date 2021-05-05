while True :
    number = input("Enter a positive number: ")
    digits = len(number)
    summ = 0
    if not number.isdigit() :
        print("It is an invalid entry. Don't use non-numeric, float, or negative values!")
    elif int(number) > 0 :
        for i in range(digits) :
            summ = summ + int(number[i]) ** digits
        if summ == int(number) :
            print(f"The number {number} is an Armstrong number")
            break
        else :
            print(f"The number {number} is not an Armstrong number")