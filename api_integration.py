
import requests

url = "https://jsonplaceholder.typicode.com/users"

try:
    response = requests.get(url, timeout=10)

    response.raise_for_status()

    data = response.json()

    if isinstance(data, list):
        print("API Connection Successful!")
        print("\nUser Details:")

        for user in data:
            print("Name:", user["name"])
            print("Email:", user["email"])
            print("-------------------")
    else:
        print("Invalid API Response!")

except requests.exceptions.Timeout:
    print("Error: Request timed out!")

except requests.exceptions.ConnectionError:
    print("Error: Please check your Internet connection!")

except requests.exceptions.HTTPError:
    print("Error: API request failed!")

except requests.exceptions.RequestException:
    print("Error: Something went wrong!")

except ValueError:
    print("Error: Invalid JSON data!")
