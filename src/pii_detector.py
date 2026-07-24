import re

EMAIL_PATTERN = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"
PHONE_PATTERN = r"\b(?:\+91[- ]?)?[6-9]\d{9}\b"
AADHAAR_PATTERN = r"\b\d{4}\s?\d{4}\s?\d{4}\b"
PAN_PATTERN = r"\b[A-Z]{5}[0-9]{4}[A-Z]\b"


def detect_pii(text):
    results = {
        "Emails": re.findall(EMAIL_PATTERN, text),
        "Phone Numbers": re.findall(PHONE_PATTERN, text),
        "Aadhaar Numbers": re.findall(AADHAAR_PATTERN, text),
        "PAN Numbers": re.findall(PAN_PATTERN, text),
    }

    return results