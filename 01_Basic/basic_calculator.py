# Basic Calculator.
num1 = int(input("Enter the number : "))
num2 = int(input("Enter the number : "))

total = 0

while True:
    op = input("Choose the operation you want to perform (+,-,*,/,%) : ")
    
    if op == "+":
        total = num1 + num2
        break
    elif op == "-":
        total = num1 - num2
        break
    elif op == "*":
        total = num1 * num2
        break
    elif op == "/":
        total = num1 / num2
        break
    elif op == "%":
        total = num1 % num2
        break
    else:
        print("Please,choose a valid option!")
        
print(f"Your total is : {total}")