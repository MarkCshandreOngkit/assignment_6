#input number(0-1000)
number = int(input("Input(0-1000): "))
if number <= 1000 and number >= 0:
    #format number to six digit
    six_digit = "{:06}".format(number)
    #print number
    print(f"Output: {six_digit}")