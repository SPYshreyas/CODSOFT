num1 = int(input("Enter First number:"))

num2 = int(input("Enter second number:"))

sign = input("ENTER any Sign(+,-,*,/):")

if sign == '+':
    res = num1 + num2  
    print(f"Added value:{res}")
elif sign == "-":
    res = num1 - num2
    print(f"Subtracted value:{res}")
elif sign == "*":
    res = num1 * num2
    print(f"Multiplied value:{res}")
else :
    res = num1 / num2
    print(f"Divided value:{res}")

