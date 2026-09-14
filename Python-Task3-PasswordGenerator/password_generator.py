import random
import string

def get_length():
    while True:
        try:
            length = int(input("Enter password length (minimum 8): "))
            if length < 8:
                print("Password length must be at least 8.")
            else:
                return length
        except ValueError:
            print("Please enter a valid whole number.")

def choose_types():
    print("\nChoose at least two character types:")
    print("1. Uppercase letters")
    print("2. Lowercase letters")
    print("3. Numbers")
    print("4. Symbols")

    while True:
        choices = input("Enter choices separated by spaces (e.g. 1 2 3 4): ").split()
        choices = set(choices)
        valid = {"1", "2", "3", "4"}

        if not choices.issubset(valid):
            print("Invalid choice. Use only 1, 2, 3, or 4.")
            continue
        if len(choices) < 2:
            print("Please select at least two character types.")
            continue
        return choices

def generate_password(length, choices):
    pools = []
    required = []

    if "1" in choices:
        pools.append(string.ascii_uppercase)
        required.append(random.choice(string.ascii_uppercase))
    if "2" in choices:
        pools.append(string.ascii_lowercase)
        required.append(random.choice(string.ascii_lowercase))
    if "3" in choices:
        pools.append(string.digits)
        required.append(random.choice(string.digits))
    if "4" in choices:
        pools.append(string.punctuation)
        required.append(random.choice(string.punctuation))

    all_characters = "".join(pools)
    remaining = [random.choice(all_characters) for _ in range(length - len(required))]
    password = required + remaining
    random.shuffle(password)
    return "".join(password)

print("=" * 45)
print("          RANDOM PASSWORD GENERATOR")
print("=" * 45)

while True:
    length = get_length()
    choices = choose_types()
    password = generate_password(length, choices)

    print("\nGenerated password:")
    print(password)

    again = input("\nGenerate another password? (y/n): ").strip().lower()
    if again != "y":
        print("Goodbye!")
        break
