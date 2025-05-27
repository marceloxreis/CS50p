import sys
import validator_collection

email = input("What's your email? ").strip()

if email.count("@") != 1:
    print("invalid")
    sys.exit(0)

username, domain = email.split("@")

if domain.count(".") < 1:
    print("invalid")
    sys.exit(1)



print("valid")
