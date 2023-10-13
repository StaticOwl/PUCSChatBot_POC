import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer, TextDataset, DataCollatorForLanguageModeling, Trainer, TrainingArguments

# Load the pretrained GPT-2 model and tokenizer
model_name = "gpt2"  # You can choose a different model if needed
model = GPT2LMHeadModel.from_pretrained(model_name).to('cuda:0')
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

# from transformers import RobertaForCausalLM, RobertaTokenizer

# # Load the RoBERTa model and tokenizer
# model_name = "roberta"
# model = RobertaForCausalLM.from_pretrained("roberta").to('cuda:0')  # Move to GPU
# tokenizer = RobertaTokenizer.from_pretrained("roberta")


# Collect and preprocess your data (replace with actual data collection and preprocessing)
data = "/content/tokenized_webpage_data.txt"

# Tokenize and format the data for training
train_dataset = TextDataset(tokenizer=tokenizer, file_path=dict_faq, block_size=128)

# Define training arguments
training_args = TrainingArguments(
    output_dir="./fine-tuned-model1",
    overwrite_output_dir=True,
    num_train_epochs=50,
    per_device_train_batch_size=128,
    save_steps=10_000,
    save_total_limit=2,
)

# Prepare the data collator
data_collator = DataCollatorForLanguageModeling(
    tokenizer=tokenizer, mlm=False,
)

# Create a Trainer and fine-tune the model
trainer = Trainer(
    model=model,
    args=training_args,
    data_collator=data_collator,
    train_dataset=train_dataset,
)

# Fine-tune the model
trainer.train()

# Save the fine-tuned model
trainer.save_model()