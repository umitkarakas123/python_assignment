number = input("Enter a positive number: ")
topno = len(str(number))
total = 0
if number.isdecimal() == False or type(number) == float or int(number) <= 0 :
    print("It is an invalid entry. Don't use non-numeric, float, or negative values!")
elif int(number) > 0 :
    i = int(number)
    for x in range(0, int(topno)):
        figure = i % 10
        total += figure ** int(topno)
        i //= 10
    if(int(number) == int(total)) :
        print(f"The number {number} is an Armstrong number")
    else:
        print(f"The number {number} is not an Armstrong number")