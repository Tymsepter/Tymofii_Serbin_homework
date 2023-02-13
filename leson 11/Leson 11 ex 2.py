import json
import sys

# Check if the JSON file exists
try:
    with open(sys.argv[1]) as f:
        phonebook = json.load(f)
except FileNotFoundError:
    phonebook = {}


# Helper function to search for a key in the phonebook
def search(key, value):
    results = []
    for entry in phonebook.values():
        if value in entry.get(key, ''):
            results.append(entry)
    return results


# Main loop
while True:
    print("1. Add new entry")
    print("2. Search by first name")
    print("3. Search by last name")
    print("4. Search by full name")
    print("5. Search by telephone number")
    print("6. Search by city or state")
    print("7. Search by gender")
    print("8. Search by company")
    print("9. Search by age")
    print("10. Delete a record for a given telephone number")
    print("11. Update a record for a given telephone number")
    print("12. Add notes or tags to an entry")
    print("13. Add email address to an entry")
    print("14. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        # Add new entry
        entry = {}
        entry['first_name'] = input("First name: ")
        entry['last_name'] = input("Last name: ")
        entry['phone_numbers'] = [input("Phone number: ")]
        entry['addresses'] = [input("Address: ")]
        entry['city'] = input("City: ")
        entry['state'] = input("State: ")
        entry['gender'] = input("Gender: ")
        entry['company'] = input("Company: ")
        entry['age'] = input("Age: ")
        entry['notes'] = input("Notes: ")
        entry['email'] = input("Email: ")
        phonebook[entry['phone_numbers'][0]] = entry
    elif choice == "2":
        # Search by first name
        query = input("Enter first name: ")
        results = search('first_name', query)
        for result in results:
            print(result)
    elif choice == "3":
        # Search by last name
        query = input("Enter last name: ")
        results = search('last_name', query)
        for result in results:
            print(result)
    elif choice == "4":
        # Search by full name
        query = input("Enter full name: ")
        results = []
        for entry in phonebook.values():
            full_name = entry['first_name'] + ' ' + entry['last_name']
            if query in full_name:
                results.append(entry)
        for result in results:
            print(result)
    elif choice == "5":
        # Search by telephone number
        query = input("Enter phone number: ")
        results = search('phone_numbers', query)
        for result in results:
            print(result)
    elif choice == "6":
        # Search by city or state
        query = input("Enter city or state: ")
        results = []
        for entry in phonebook.values():
            if query in entry['city'] or query in entry['state']:
                results.append(entry)
        for result in results:
            print(result)
    elif choice == "7":
        # Search by gender
        query = input("Enter gender: ")
        results = search('gender', query)
        for result in results:
            print(result)
    elif choice == "8":
        print("Goodbye")
