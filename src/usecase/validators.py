def is_valid_email(email: str) -> bool:
    if not email:
        return False
    if "@" not in email:
        return False
    return True
def is_valid_name(name: str) -> bool:
    if not name:
        return False

    if len(name) < 2:
        return False

    # NEW minimal rule: no digits inside name
    if any(char.isdigit() for char in name):
        return False

    return True


