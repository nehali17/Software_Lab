import re

def is_valid_email(email):
    # Check if input is a string
    if not isinstance(email, str):
        return False

    # Check for empty email
    if email == "":
        return False

    # Check for whitespace characters
    if any(c.isspace() for c in email):
        return False

    # Email should contain only one @
    if email.count("@") != 1:
        return False

    # Split email into username and domain
    username, domain = email.split("@")

    # Username and domain should not be empty
    if username == "" or domain == "":
        return False

    # Username should not start with a dot
    if username.startswith("."):
        return False

    # No two dots together
    if ".." in email:
        return False

    # Hyphen is not allowed in username
    if "-" in username:
        return False

    # Check username characters
    if not re.match(r"^[A-Za-z0-9._%+]+$", username):
        return False

    # Domain should not start or end with a dot
    if domain.startswith(".") or domain.endswith("."):
        return False

    # Domain should have a dot
    if "." not in domain:
        return False

    # Check domain parts
    parts = domain.split(".")

    for part in parts:
        if part == "":
            return False

        # Domain cannot start or end with hyphen
        if part.startswith("-") or part.endswith("-"):
            return False

        # Domain parts should only contain alphanumeric characters and hyphens
        if not re.match(r"^[A-Za-z0-9-]+$", part):
            return False

    # Extension should have at least 2 letters
    if not re.match(r"^[A-Za-z]{2,}$", parts[-1]):
        return False

    return True


# Take email from user
email = input("Enter your email: ")

# Display result
if is_valid_email(email):
    print("Valid Email")
else:
    print("Invalid Email")
