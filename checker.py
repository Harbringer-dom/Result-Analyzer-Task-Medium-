def check_password_strength(x):
    # Store each password rule as True/False.
    checks = {
        "At least 8 characters long": len(x) >= 8,
        "At least one digit": any(c.isdigit() for c in x),
        "At least one uppercase letter": any(c.isupper() for c in x),
        "At least one lowercase letter": any(c.islower() for c in x),
        "At least one special character": any(not c.isalnum() for c in x),
    }

    # Count how many checks passed.
    passed_count = sum(checks.values())

    # Rate the password based on total passed checks.
    if passed_count <= 1:
        strength = "Weak Password"
    elif passed_count <= 3:
        strength = "Medium Password"
    else:
        strength = "Strong Password"

    return checks, passed_count, strength


def main():
    #Ask user for input
    x = input("Enter password: ")
    checks, passed_count, strength = check_password_strength(x)
    # Checks the requirements
    print("Password Analysis:")
    for criteria, passed in checks.items():
        print(f"{criteria}: {'pass' if passed else 'fail'}")
    # Print the result
    print(f"Passed criteria count: {passed_count}")
    print(f"Overall password strength: {strength}")
  

if __name__ == "__main__":
    main()

