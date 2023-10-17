import json
import os
from pytorch_pretrained_bert import cached_path

# url = "https://s3.amazonaws.com/datasets.huggingface.co/personachat/personachat_self_original.json"


def load_data_to_json(url=None, file_path=None):
    data = None
    if url:
        file_path = cached_path(url)
    with open(file_path, "r", encoding="utf-8") as f:
            data = json.loads(f.read())
    if data:
        return data
    else:
        raise Exception("No input source provided.")


def process_input_json(dataset = None, data_types = ['train', 'valid']):
    if not dataset:
        raise Exception("Dataset is empty.")
    os.makedirs("runtime", exist_ok=True)
    for data_type in data_types:
        input_data = dataset[data_type]
        output_data = []

        for i, datum in enumerate(input_data):
            output_data.append({
                "id": f"{i:0>5}",
                **datum
            })
        with open(f"runtime/{data_type}_data.json", "w", encoding="utf-8") as f:
            for datum in output_data:
                line = json.dumps(datum, ensure_ascii=False)
                print(line, file=f)

