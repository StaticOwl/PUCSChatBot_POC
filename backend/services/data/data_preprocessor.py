import json
import os


def update_json_structure(json_data):
    if json_data[-1]['title'] == 'dummy':
        json_data['scrapped_data'].pop(-1)
    updated_json = []
    data_dict = {}
    data_key = []
    json_data.append({'title': 'dummy', 'type': 'dummy', 'context': 'dummy'})
    for data in json_data:
        if (data['title'], data['type']) not in data_key or data == json_data[-1]:
            if data_dict:
                updated_json.append(data_dict)
            data_dict = {'title': data['title'].strip(), 'type': data['type'].strip()}
            data_key.append((data['title'], data['type']))

        context_data = data['context'].split(" ")
        new_key = context_data[0].lower()
        new_value = " ".join(context_data[1:])
        data_dict[new_key] = new_value.replace('\n', '')

    print(updated_json)
    return updated_json


def insert_newline(sentence, max_chars=500):
    words = sentence.split()
    current_line = ''
    result = ''

    for word in words:
        if len(current_line + word) <= max_chars:
            current_line += word + ' '
        else:
            result += current_line.strip() + '\n'
            current_line = word + ' '

    # Add the last line
    result += current_line.strip()

    return result


def textify_data(big_data, config: dict = None):
    big_content = ""
    for data in big_data:
        content = """{title}: """.format(
            title=data['title'])
        big_content += content

    with open('para_faculty_data.txt', 'w+') as f:
        f.write(big_content)
