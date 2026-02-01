def check_password_strength(password: str) -> dict:
    result = {
        "length": False,
        "uppercase": False,
        "lowercase": False,
        "digit": False,
        "special": False,
        "is_strong": False
    }

    # Rule 1: length check
    if len(password) >= 8:
        result["length"] = True

    # Rule 2–5: character checks
    for char in password:
        if char.isupper():
            result["uppercase"] = True
        elif char.islower():
            result["lowercase"] = True
        elif char.isdigit():
            result["digit"] = True
        elif not char.isalnum():
            result["special"] = True

    # Final decision
    result["is_strong"] = all([
        result["length"],
        result["uppercase"],
        result["lowercase"],
        result["digit"],
        result["special"]
    ])

    return result


