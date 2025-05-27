def main():
    ...
    word = input("Input: ")
    replaced_word = shorten(word)
    print(f"Output: {replaced_word}")


def shorten(word):
    ...
    vowels = set('aeiouAEIOU')  # Using a set for faster lookup
    replaced_word = ''.join([char for char in word if char not in vowels])submit50 cs50/problems/2022/python/tests/twttr
    return replaced_word

if __name__ == "__main__":
    main()
