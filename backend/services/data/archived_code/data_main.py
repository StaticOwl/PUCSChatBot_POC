import data_loader as dl
if __name__ == '__main__':
    raw_data = dl.load_data_to_json("https://s3.amazonaws.com/datasets.huggingface.co/personachat/personachat_self_original.json")
    dl.process_input_json(raw_data)
    