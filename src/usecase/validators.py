def is_valid_email(email: str) -> bool:
    if not email:
        return False
    if "@" not in email:
        return False
    return True
def is_valid_name(name: str) -> bool:
    if not name:
        return False
    return True
