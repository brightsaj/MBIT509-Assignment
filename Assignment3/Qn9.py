import re


# I. Extract all email addresses from a given text
def extract_emails(text):
    # Regex pattern to match email addresses
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    return re.findall(email_pattern, text)


# II. Validate a date in the format "YYYY-MM-DD"
def validate_date(date):
    # Regex pattern to validate date format YYYY-MM-DD
    date_pattern = r'^\d{4}-\d{2}-\d{2}$'
    if re.match(date_pattern, date):
        # Further check for valid date logic can be added
        return True
    return False


# III. Replace all occurrences of a word with another word in a string
def replace_word(text, old_word, new_word):
    # Regex pattern to match the whole word (case-sensitive)
    word_pattern = r'\b' + re.escape(old_word) + r'\b'
    return re.sub(word_pattern, new_word, text)


# IV. Split a string by all non-alphanumeric characters
def split_by_non_alphanumeric(text):
    # Regex pattern to split the string by non-alphanumeric characters
    return re.split(r'[^a-zA-Z0-9]+', text)


# Test the functions
if __name__ == "__main__":
    # Test case for extracting emails
    text = "Contact us at support@example.com or sales@company.org for inquiries."
    emails = extract_emails(text)
    print("Extracted Emails:", emails)

    # Test case for validating date
    date = "2025-03-18"
    is_valid = validate_date(date)
    print(f"Is '{date}' a valid date?", is_valid)

    # Test case for replacing a word
    sentence = "The quick brown fox jumps over the lazy dog."
    new_sentence = replace_word(sentence, "fox", "cat")
    print("Updated Sentence:", new_sentence)

    # Test case for splitting by non-alphanumeric characters
    string = "Hello! How are you? I'm fine, thanks."
    split_result = split_by_non_alphanumeric(string)
    print("Split Result:", split_result)