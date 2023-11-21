import re


def extract_to_dict(text):
    """
    Extracts terms and sentences from a given text and stores them in a dictionary.

    :param text: String containing the text to be processed.
    :return: Dictionary with extracted terms and sentences or a message if not found.
    """
    # Find the substring starting with "Output list:"
    output_list_start = text.find("Output list:")
    if output_list_start == -1:
        return "Output list not found"

    output_list_text = text[output_list_start:]

    pattern = r'(Term \d+|Sent \d+): (.*?)($|, )'

    # Find all matches in the output list text
    matches = re.findall(pattern, output_list_text)

    extracted_dict = {}

    for match in matches:
        key, value, _ = match
        extracted_dict[key.strip()] = value.strip()

    return extracted_dict
