import requests
import sys

try:
    # Check if the user has provided the required argument
    if len(sys.argv) != 2:
        print("Missing command-line argument")
        sys.exit(1)

    # Ensure the amount is a float for better precision
    amount = sys.argv[1]
    if not amount.replace('.', '', 1).isdigit():  # Check if it's a number
        print("Command-line argument is not a number")
        sys.exit(1)
    amount = float(amount)  # Use float to support decimal values

    # Fetch the Bitcoin price from the API
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for HTTP errors

    # Parse the JSON response
    data = response.json()
    rate = float(data["bpi"]["USD"]["rate"].replace(",", ""))  # Bitcoin price in USD

    # Calculate the equivalent value in USD for the given amount of Bitcoin
    usd_value = amount * rate

    # Output the USD equivalent of the Bitcoin amount
    print(f"${usd_value:,.4f}")  # Print the value in USD with 2 decimal places

except requests.RequestException:
    print("Error: Unable to fetch Bitcoin price.")
    sys.exit(1)
except ValueError:
    print("Error: Invalid input.")
    sys.exit(1)
