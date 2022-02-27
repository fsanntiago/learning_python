# 7-9. No Pastrami: Using the list sandwich_orders from Exercise 7-8,
# make sure the sandwich 'pastrami' appears in the list at least three
# times. Add code near the beginning of your program to print a message
# saying the deli has run out of pastrami, and then use a while loop to
# remove all occurrences of 'pastrami' from sandwich_orders. Make sure
# no pastrami sandwiches end up in finished_sandwiches.

sandwiches_orders = [
    'roast beef', 'pastrami', 'grilled chicken', 'pastrami',
    'cheese', 'eggs', 'pastrami']
finished_sandwiches = []

print("I'm sorry, we're all out of pastrami today.")
while 'pastrami' in sandwiches_orders:
    sandwiches_orders.remove('pastrami')

print("\n")
while sandwiches_orders:
    current_sandwich = sandwiches_orders.pop()
    print(f"I'm working on your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\n")
# Display sanwiches
for sandwich in finished_sandwiches:
    print(f"- I made a {sandwich} sandwich.")
