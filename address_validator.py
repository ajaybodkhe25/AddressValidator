def validate(address):
    dot = address.find(".")
    at = address.find("@")

    if dot == -1 or at == -1:
        return "Invalid Email"
    else:
        return "Valid Email"
