# print("Hello, World!")
# print("Hello, name!")
# input("What's your name? ")
# print("Hello, World")

# Ask user's name...
name = input("What's your name? ")

# Say hello to the user...
# print("Hello, name")
print("Hello, ") # By default, print() has an 'end=\n', so we can overwritte as end="" to avoid line break...
print(name)

# Say hello to user in a better manner...
print("Hello, world!")
print('Hello, \"friend"')
name = input("What is your name? ")
print("Hello, " + name)
print("Hello,",name)
print(f"Hello, {name}")
# If user uses too many spaces before and after name...
name = name.strip() # Strip blank spaces before and after strings...
print("Hello, without spaces, Mr. " + name)
name = name.capitalize() # Capitaliza only the first letter of the first word...
print("Hello, without spaces, and now capitalized Mr. " + name)
name = name.title() # Capitalize all the first letters of various words...
print("Hello, without spaces, and now capitalized, but in all the names Mr. " + name)

# I have used "Methods" in the variable name...
name = input("Finally, what is your full name? ").strip().title()
print(f"Hello, Mr. {name}!")

# Split user's name into first name and last name...
firstName, lastName = name.split(" ")
print(f"Hello, {firstName}, or should I say Mr. {lastName}?")

