'''Archived method. Will write something new here.'''

import json
import os
from pytorch_pretrained_bert import cached_path
from data import InputData

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
    return_data = []
    for data_type in data_types:
        data = InputData()
        input_data = dataset[data_type]
        output_data = []

        for i, datum in enumerate(input_data):
            output_data.append({
                "id": f"{i:0>5}",
                **datum
            })
        
#           with open(f"runtime/{data_type}_data.json", "w", encoding="utf-8") as f:
#             for datum in output_data:
#                 line = json.dumps(datum, ensure_ascii=False)
#                 print(line, file=f)

        data.set_data(data_type, output_data)
        return_data.append(data)

    return return_data

def persona_formatting(data:InputData, **args):
    input_data = data.update(args)
    utterance_output = []
    for datum in input_data.data:
        persona = datum["personality"].copy()

        for _ in range(repeat):
            for i, utterance in enumerate(datum["utterances"]):
                if permute:
                    shuffle(persona)
                your_persona = " ".join(persona)
                
                history = utterance["history"]
                candidates = utterance["candidates"]

                if not tag:
                    history_tagged = [s for s in history[-(2*input_data.max_history+1):]]
                else:
                    history_tagged = [("<parter>" if (len(history)-i) % 2 else "<you>") + ' ' + s for i, s in 
                    enumerate(history[-(2*input_data.max_history+1):])]
                index = f"{datum['id']}-{i:02}"
                output_data.append({"id": index, "context": your_persona, "input": " ".join(history_tagged), "target": candidates[-1]})

            

def utterance_formatting_for_fid(data:InputData, **args):
    input_data = data.update(args)
    utterance_output = []
    for datum in input_data.data:
        personas = datum['personality']
        my_personas = [" ".join(personas[i*input_data.num_personas_per_prefix: (i+1)*input_data.num_personas_per_prefix]) \
                            for i in range(0, int(len(personas) / input_data.num_personas_per_prefix))] \
                            if input_data.long_prefix else [" ".join(personas)]

        dialog_output_data = []
        for i, utterance in enumerate(datum["utterances"]):
            history = utterance["history"]
            candidates = utterance["candidates"]

            if not tag:
                history_tagged = [s for s in history[-(2*input_data.max_history+1):]]
            else:
                history_tagged = [("<parter>" if (len(history)-i) % 2 else "<you>") + ' ' + s for i, s in enumerate(history[-(2*input_data.max_history+1):])]
            index = f"{datum['id']}-{i:02}"
            ctxs = [{"title": "", "text": persona} for persona in my_personas]
            dialog_output_data.append({"id": index, "ctxs": ctxs, "question": " ".join(history_tagged), "target": candidates[-1]})

        utterance_output.extend(dialog_output_data)

    input_data.update("utterance", utterance_output)
    
    return input_data


