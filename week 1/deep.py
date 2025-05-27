x = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")

# Normalize the input
normalized = x.lower().replace(" ", "").replace("-", "")

# Check for various valid answers
if normalized == "fortytwo" or normalized == "42":
    print("yes")
else:
    print("no")
