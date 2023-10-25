# CREDITS-CHATGPT
import torch
from transformers import (
    GPT2LMHeadModel,
    GPT2Tokenizer,
    TextDataset,
    DataCollatorForLanguageModeling,
    Trainer,
    TrainingArguments,
)

def load_model_and_tokenizer(model_name, device):
    model = GPT2LMHeadModel.from_pretrained(model_name).to(device)
    tokenizer = GPT2Tokenizer.from_pretrained(model_name)
    return model, tokenizer

def preprocess_data(data_path, tokenizer, block_size=128):
    dataset = TextDataset(tokenizer=tokenizer, file_path=data_path, block_size=block_size)
    return dataset

def train_model(model, train_dataset, training_args):
    data_collator = DataCollatorForLanguageModeling(tokenizer=model.config, mlm=False)
    trainer = Trainer(
        model=model,
        args=training_args,
        data_collator=data_collator,
        train_dataset=train_dataset,
    )
    trainer.train()
    trainer.save_model()

if __name__ == "__main__":
    model_name = "gpt2"  # Change to the desired model name
    data_path = "/content/tokenized_webpage_data.txt"

    # Load the model and tokenizer
    device = 'cuda:0' if torch.cuda.is_available() else 'cpu'
    model, tokenizer = load_model_and_tokenizer(model_name, device)

    # Preprocess the data
    train_dataset = preprocess_data(data_path, tokenizer)

    # Define training arguments
    training_args = TrainingArguments(
        output_dir="./fine-tuned-model1",
        overwrite_output_dir=True,
        num_train_epochs=50,
        per_device_train_batch_size=128,
        save_steps=10_000,
        save_total_limit=2,
    )

    # Train the model
    train_model(model, train_dataset, training_args)
