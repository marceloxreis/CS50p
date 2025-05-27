word = input("Input: ")
vowels = set('aeiouAEIOU')  # Using a set for faster lookup
replaced_word = ''.join([char for char in word if char not in vowels])
print(f"Output: {replaced_word}")
