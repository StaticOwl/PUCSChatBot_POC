import json
from pytorch_pretrained_bert import cached_path


def load_data_to_json(url=None, file_path=None):
    data = None
    if url:
        file_path = cached_path(url)
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.loads(f.read())
    elif file_path:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.loads(f.read())

url = "https://s3.amazonaws.com/datasets.huggingface.co/personachat/personachat_self_original.json"
personachat_file = cached_path(url)

with open(personachat_file, "r", encoding="utf-8") as f:
    data = json.loads(f.read())