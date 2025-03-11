def check_number(num):
    if num == 0:
        print("0 is neither positive nor negative. It is an Even number.")
    elif num > 0:
        if num % 2 == 0:
            print(f"{num} is a Positive Even number.")
        else:
            print(f"{num} is a Positive Odd number.")
    else:
        if num % 2 == 0:
            print(f"{num} is a Negative Even number.")
        else:
            print(f"{num} is a Negative Odd number.")
try:
    number = int(input("Enter a number: "))
    check_number(number)
except ValueError:
    print("Invalid input. Please enter a valid number.")
