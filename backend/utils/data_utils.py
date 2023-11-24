"""
This file contains utility functions for data processing.
"""


def update_keys_with_substring(data, substring, new_value):
    """
    This method is used to update the keys of a dictionary with a substring.
    :param data: dictionary to be updated.
    :param substring: string to be replaced.
    :param new_value: replacement string.
    :return: dictionary with updated keys.
    """
    updated_data = data.copy()
    for key, value in data.items():
        if substring in key:
            key = key.replace(substring, new_value)
            value = value.replace(substring, new_value)
        updated_data[key] = value

    return updated_data


def insert_newline(sentence, max_chars=500):
    """
    This method is used to insert a newline character in a sentence after a certain number of characters.
    This method is created to limit the PalmAPI's input size, as free APIs have a limit of 1000 characters.
    :param sentence: text to be processed.
    :param max_chars: maximum number of characters in a line.
    :return: reduced text.
    """
    lines = sentence.split('\n')
    result = []

    for line in lines:
        words = line.split()
        current_line = ''

        for word in words:
            if len(current_line + word) + 1 <= max_chars:  # Add 1 for the space
                current_line += word + ' '
            else:
                result.append(current_line.strip())
                current_line = word + ' '

        # Add the last line
        result.append(current_line.strip())

    return '\n'.join(result)


def safe_replace(string, replacement: dict = None):
    """
    This method is used to replace the string with the replacement dictionary.
    :param string: string to be replaced.
    :param replacement: replacement dictionary.
    :return: updated string.
    """
    if replacement is not None:
        for k, v in replacement.items():
            string = string.replace(k, v)
    return string
