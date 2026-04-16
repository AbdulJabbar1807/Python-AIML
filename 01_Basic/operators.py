# Can you drive?
age = int(input("Enter your age : "))
while True:
    is_license = input("Do you have driving license (yes/no) : ")
    if is_license.lower() == "yes":
        is_license = True
        break
    elif is_license.lower() == "no":
        is_license = False
        break
    else:
        print("Please enter a valid choice (yes/no)-")

can_drive = age>=18 and is_license

can_drive = age>=18 and is_license  
if can_drive:
    print("You can drive!")
else:
    print("You can't drive!")