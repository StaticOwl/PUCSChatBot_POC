def update_keys_with_substring(data, substring, new_value):
    updated_data = data.copy()
    for key, value in data.items():
        if substring in key:
            key = key.replace(substring, new_value)
            value = value.replace(substring, new_value)
        updated_data[key] = value

    return updated_data


def insert_newline(sentence, max_chars=500):
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
    if replacement is not None:
        for k, v in replacement.items():
            string = string.replace(k, v)
    return string
