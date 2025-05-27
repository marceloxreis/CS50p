# Initialize an empty list to store user inputs
user_inputs = []

try:
    # Collect inputs from the user
    while True:
        item = input().strip().upper()
        user_inputs.append(item)  # Store each input in the list
except EOFError:
    # Initialize a dictionary to count occurrences
    counts = {}

    # Count occurrences of each item in the list
    for item in user_inputs:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1

    # Sort the dictionary by keys and print each item with its count
    for item in sorted(counts):
        print(f"{counts[item]} {item}")
