import re


def validate_password(password):
    pattern = r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
    return re.match(pattern, password) is not None


def validate_email(email):
    pattern = r"^[a-zA-Z][a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    return re.match(pattern, email) is not None


def validate_country_code(code):
    pattern = r"^\+\d{1,4}$"
    return re.match(pattern, code) is not None


def validate_contact_number(contact_number):
    pattern = r"^[6-9]\d{9}$"
    return re.match(pattern, contact_number) is not None


def validate_person_name(name):
    pattern = r"^[a-zA-Z][a-zA-Z][a-zA-Z ]+(([\'\,\.\-][a-zA-Z])?[a-zA-Z]*)*$"
    return re.match(pattern, name) is not None
