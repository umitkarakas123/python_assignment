number = input("Enter a number : ")
prime_number = []
not_prime = []
if number.isdecimal() == False or type(number) == float or int(number) <= 1 :
    print("It is an invalid entry. Don't use non-numeric, float, or negative values!")
elif int(number) > 1 :
    for i in range (2, int(number)+1):
        for j in range(2, i):
            if i % j == 0:
                not_prime.append(i)
                break
        else:
            prime_number.append(i)
    print("Prime number:",prime_number)
    print("Prime not number:",not_prime)