from transformers import GPT2LMHeadModel, GPT2Tokenizer, TextDataset, DataCollatorForLanguageModeling
from torch.utils.data import DataLoader
import torch

class ChatGPT:
    def __init__(self):
        self.model_name = "gpt2"
        self.tokenizer = GPT2Tokenizer.from_pretrained(self.model_name)
        self.model = GPT2LMHeadModel.from_pretrained(self.model_name)
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model.to(self.device)

    def send_prompt(self, prompt):
        input_ids = self.tokenizer.encode(prompt, return_tensors="pt").to(self.device)
        output = self.model.generate(input_ids, max_length=50, num_return_sequences=1)
        response = self.tokenizer.decode(output[0], skip_special_tokens=True)
        return response

    def update_model(self, text_data):
        dataset = TextDataset(
            tokenizer=self.tokenizer,
            file_path=text_data,  # Path to a text file containing training data
            block_size=128
        )
        data_collator = DataCollatorForLanguageModeling(
            tokenizer=self.tokenizer, mlm=False
        )
        train_loader = DataLoader(dataset, batch_size=8, collate_fn=data_collator)

        optimizer = torch.optim.AdamW(self.model.parameters(), lr=5e-5)
        for epoch in range(3):  # Train for 3 epochs as an example
            self.model.train()
            for batch in train_loader:
                inputs, labels = batch["input_ids"].to(self.device), batch["labels"].to(self.device)
                outputs = self.model(inputs, labels=labels)
                loss = outputs.loss
                loss.backward()
                optimizer.step()
                optimizer.zero_grad()
        print("Model updated successfully.")


def main():
    chatbot = ChatGPT()

    prompt = "How are you?"
    response = chatbot.send_prompt(prompt)
    print("Response:", response)

    text_data = "text_data.txt"  # Path to a text file containing additional training data
    chatbot.update_model(text_data)

# Send another prompt after updating
    prompt = "What's your favorite color?"
    response = chatbot.send_prompt(prompt)
    print("Response:", response)

if __name__ == "__main__":
    main()
