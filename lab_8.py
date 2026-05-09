# !pip install langchain cohere langchain-community google-colab

# !pip install langchain-cohere

import cohere
import getpass
from langchain import PromptTemplate
from langchain_cohere import ChatCohere
from langchain_core.messages import HumanMessage
from google.colab import auth
from google.colab import drive

auth.authenticate_user()
drive.mount('/content/drive')

file_path = "/content/drive/MyDrive/GenAI/sample.txt"

try:
  with open(file_path, "r", encoding="utf-8") as file:
    text_content = file.read()
    print(" File loaded successfully!")
except Exception as e:
  print(" Error loading file:", str(e))

COHERE_API_KEY = getpass.getpass("Enter your Cohere API Key: ")

cohere_llm = ChatCohere(
    cohere_api_key=COHERE_API_KEY,
    model="command-a-03-2025"
)

template = """
You are an AI assistant helping to summarize and analyze a text document.
Here is the document content:
{text}
* Summary: - Provide a concise summary of the document.
* Key Takeaways: - List 3 important points from the text.
* Sentiment Analysis: - Determine if the sentiment of the document is Positive, Negative, or Neutral.
"""
prompt_template = PromptTemplate(input_variables=["text"],template=template)

formatted_prompt = prompt_template.format(text=text_content)
print("formatted_prompt := ",formatted_prompt)

response = cohere_llm.invoke([HumanMessage(content=formatted_prompt)]).content
print("\nFormatted Output\n")
print(response)

