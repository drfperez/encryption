import re

# Function to calculate the EAN13 check digit
def calculate_ean13_check_digit(number):
    if len(number) != 12:
        raise ValueError("EAN13 number must have 12 digits")
    factor = [1, 3] * 6
    total = sum(int(digit) * factor[index] for index, digit in enumerate(number))
    check_digit = (10 - (total % 10)) % 10
    return check_digit

# Function to calculate the ISBN-13 check digit
def calculate_isbn13_check_digit(number):
    if len(number) != 12:
        raise ValueError("ISBN-13 number must have 12 digits")
    factor = [1, 3] * 6
    total = sum(int(digit) * factor[index] for index, digit in enumerate(number))
    check_digit = (10 - (total % 10)) % 10
    return check_digit

# Function to calculate the GS1-128 check digit
def calculate_gs1128_check_digit(number):
    if len(number) != 17:
        raise ValueError("GS1-128 number must have 17 digits")
    factor = [1, 3] * 8
    total = sum(int(digit) * factor[index] for index, digit in enumerate(number))
    check_digit = (10 - (total % 10)) % 10
    return check_digit

# Function to validate the EAN13 number
def validate_ean13(number):
    if not re.match(r'^\d{13}$', number):
        return False
    check_digit = calculate_ean13_check_digit(number[:-1])
    return check_digit == int(number[-1])

# Function to validate the ISBN-13 number
def validate_isbn13(number):
    if not re.match(r'^\d{13}$', number):
        return False
    check_digit = calculate_isbn13_check_digit(number[:-1])
    return check_digit == int(number[-1])

# Function to validate the GS1-128 number
def validate_gs1128(number):
    if not re.match(r'^\d{17}$', number):
        return False
    check_digit = calculate_gs1128_check_digit(number[:-1])
    return check_digit == int(number[-1])

# Main function
def main():
    # Prompt user for code type and code
    code_type = input("Enter 1 for EAN13, 2 for GS1-128, or 3 for ISBN: ")
    code = input("Enter the code: ")

    # Validate code and output result
    if code_type == "1":
        if validate_ean13(code):
            print("Correct EAN13 number")
        else:
            check_digit = calculate_ean13_check_digit(code[:-1])
            print(f"Incorrect EAN13 number, correct check digit is {check_digit}")
    elif code_type == "2":
        if validate_gs1128(code):
            print("Correct GS1-128 number")
        else:
            check_digit = calculate_gs1128_check_digit(code[:-1])
            print(f"Incorrect GS1-128 number, correct check digit is {check_digit}")
    elif code_type == "3":
        if validate_isbn13(code):
            print("Correct ISBN-13 number")
        else:
            check_digit = calculate_isbn13_check_digit(code[:-])
            print(f"Incorrect ISBN-13 number, correct check digit is {check_digit}")
    else:
        print("Invalid code type")
    
if __name__ == '__main__':
    main()
