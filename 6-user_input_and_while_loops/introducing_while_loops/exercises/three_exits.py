# 7-6. Three Exits: Write different versions of either Exercise 7-4 or
# Exercise 7-5 that do each of the following at least once:
# •	 Use a conditional test in the while statement to stop the loop.
# •	 Use an active variable to control how long the loop runs.
# •	 Use a break statement to exit the loop when the user enters a
# 'quit' value.

prompt = "\nHow old are you?"
prompt += "\nEnter 'quit' when you are finished: "

# Condicional test in while statement
# age = ""
# while age != 'quit':
#     age = input(prompt)
#     if age != 'quit':
#         age = int(age)
#         if age < 3:
#             print("The ticket is free.")
#         elif age < 13:
#             print("The ticket is $10.")
#         else:
#             print("The ticket is $15.")

# Using an active variable to control how long the loop runs
# active = True
# while active:
#     age = input(prompt)
#     if age == 'quit':
#         active = False
#     else:
#         age = int(age)
#         if age < 3:
#             print("The ticket is free.")
#         elif age < 13:
#             print("The ticket is $10.")
#         else:
#             print("The ticket is $15.")

# Using a break statement to exit the loop when the user enters a
# 'quit' value
while True:
    age = input(prompt)
    if age == 'quit':
        break
    else:
        age = int(age)
        if age < 3:
            print("The ticket is free.")
        elif age < 13:
            print("The ticket is $10.")
        else:
            print("The ticket is $15.")
