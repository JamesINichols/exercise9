def checkPasswordComplexity(password):
    # Define length requirements
    min_length = 8
    max_length = 20
    
    has_uppercase = False
    has_lowercase = False
    has_digit = False
    has_special = False
    special_characters = "!@#$%^&*(),.?\":{}|<>"
    
    # Check length of password
    if len(password) <= min_length or len(password) >= max_length:
        return False, f"Password must be between {min_length} and {max_length} characters long."
    
    # Check for required types of characters
    for char in password:
        if char.isupper():
            has_uppercase = True
        if char.islower():
            has_lowercase = True
        if char.isdigit():
            has_digit = True
        if char in special_characters:
            has_special = True

    # Check if all requirements are met
    if not has_uppercase:
        return False, "Password must contain at least one uppercase letter."
    if not has_lowercase:
        return False, "Password must contain at least one lowercase letter."
    if not has_digit:
        return False, "Password must contain at least one digit."
    if not has_special:
        return False, "Password must contain at least one special character."

    return True, "Password is complex enough."

def main():
    password = input("Enter your password: ")
    is_valid, message = checkPasswordComplexity(password)
    print(message)

if __name__ == "__main__":
    main()
