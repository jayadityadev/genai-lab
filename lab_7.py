from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

model_name = "sshleifer/distilbart-cnn-12-6"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

text = """Air pollution is one of the biggest environmental health risks. Pollutants can be gases, like ozone or nitrogen oxides, or small particles, like soot and dust. Outdoor air pollution comes from burning fossil fuels for electricity and transport. Indoor air pollution is often from burning firewood or coal for cooking and heating. Long-term exposure to polluted air can cause respiratory diseases, heart problems, and other serious health issues."""

inputs = tokenizer.encode(text, return_tensors="pt", max_length=512, truncation=True)

summary_ids = model.generate(
    inputs,
    max_length=50,
    min_length=30,
    length_penalty=2.0,
    num_beams=4,
    early_stopping=True
)

summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)
print("Summary:", summary)