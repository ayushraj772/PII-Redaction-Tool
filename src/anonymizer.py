from faker import Faker

fake = Faker()


def anonymize_text(text, presidio_results):
    replacements = {}

    # Reverse order so indices don't shift
    presidio_results = sorted(
        presidio_results,
        key=lambda x: x.start,
        reverse=True
    )

    for result in presidio_results:

        entity = result.entity_type

        if entity == "PERSON":
            fake_value = fake.name()

        elif entity == "EMAIL_ADDRESS":
            fake_value = fake.email()

        elif entity == "PHONE_NUMBER":
            fake_value = fake.phone_number()

        elif entity == "ORGANIZATION":
            fake_value = fake.company()

        else:
            # Skip LOCATION, DATE_TIME, URL, etc.
            continue

        original = text[result.start:result.end]

        if original not in replacements:
            replacements[original] = fake_value

        text = (
            text[:result.start]
            + replacements[original]
            + text[result.end:]
        )

    return text, replacements