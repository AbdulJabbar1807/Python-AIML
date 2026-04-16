first_name = "Abdul"
middle_name = "Jabbar"
last_name = "Khokhar"

name = (first_name +" "+ middle_name + " " +last_name)
print(name)
print("-"*20)

print(len(name))

age = 21
can_vote = age>=18 # Conditional operator.
print(can_vote)
if can_vote:
    print("You can vote.")
else:
    print("You can't vote.")

# String methods
print(name.lower())
print(name.upper())
print(name.title())
print(name.capitalize())
print(name.casefold())
print(name.count("a"))