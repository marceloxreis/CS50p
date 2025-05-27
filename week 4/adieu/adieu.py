# Initialize an empty list to store user inputs
user_inputs = []

try:
    # Collect inputs from the user
    while True:
        name = input()
        user_inputs.append(name)  # Store each input in the list
except EOFError:
    length = len(user_inputs)

    if length == 1:
        print("Adieu, adieu, to " + user_inputs[0])  # Print the single input
    elif length == 2:
        print("Adieu, adieu, to " + " and ".join(user_inputs))  # Join two names with 'and'
    elif length > 2:
        print("Adieu, adieu, to " + ", ".join(user_inputs[:-1]) + f", and {user_inputs[-1]}")  # Properly format the list
