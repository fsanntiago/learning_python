# 7-8. Deli: Make a list called sandwich_orders and fill it with the
# names of various sandwiches. Then make an empty list called sandwich
# finished_sandwiches. Loop through the list of sandwich orders and
# print a message for each order, such as I made your tuna sandwich. As
# each sandwich is made, move it to the list of finished sandwiches.
# After all the sandwiches have been made, print a message listing each
# sandwich that was made.

sandwiches_orders = ['roast beef', 'grilled chicken', 'cheese', 'eggs']
finished_sandwiches = []

# Move items from sandwiches_orders to finished_sandwiches
while sandwiches_orders:
    current_sandwich = sandwiches_orders.pop()
    print(f"I'm working your {current_sandwich} sandwich.")

    finished_sandwiches.append(current_sandwich)

print("\n")
# Display sanwiches
for sandwich in finished_sandwiches:
    print(f"- I made a {sandwich} sandwich.")
