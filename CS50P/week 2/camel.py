word = input("camelCase: ")
replaced_word = ''.join(['_' + char.lower() if char.isupper() else char for char in word]).lstrip('_')
print(f"snake_case: {replaced_word}")
