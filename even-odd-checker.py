# even_odd_checker.py

def check_even_odd(num):
    if num % 2 == 0:
        return f"{num} is even"
    else:
        return f"{num} is odd"

def is_valid_integer(input_str):
    try:
        int(input_str)
        return True
    except ValueError:
        return False

def main():
    while True:
        user_input = input("Enter a number: ")
        if is_valid_integer(user_input):
            num = int(user_input)
            print(check_even_odd(num))
            break
        else:
            print("Invalid input. Please enter a valid integer.")

if _name_ == "_main_":
    main()
