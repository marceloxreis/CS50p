def get_output(input_item, dictionary):
    # Check if the input item exists as a key in the dictionary
    if input_item in dictionary:
        return dictionary[input_item]

# Example dictionary with item pairs (calories per item)
items_dict = {
    "apple": "130",
    "avocado": "50",
    "banana": "110",
    "cantaloupe": "50",
    "grapefruit": "60",
    "grapes": "90",
    "melon": "50",
    "kiwifruit": "90",
    "lemon": "15",
    "lime": "20",
    "nectarine": "60",
    "orange": "80",
    "peach": "60",
    "pear": "100",
    "pineapple": "50",
    "plums": "70",
    "strawberries": "50",
    "sweet cherries": "100",
    "tangerine": "50",
    "watermelon": "80",
}

# Example input and output
input_item = input("Item: ").lower()
output_item = get_output(input_item, items_dict)

# Print the output
if output_item:
    print(f"Calories: {output_item}")
