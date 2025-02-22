import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env
load_dotenv()

# Instantiate the client with your API key
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def simplified_summarization_agent(text):
    """
    Generates a summary using simple, clear language suitable for a broad audience.
    """
    # Updated prompt: Instruct the model to simplify language
    prompt = (
        "Please summarize the following text in simple, clear language for a broad audience. "
        "Use short sentences and avoid complex vocabulary.\n\n"
        f"{text}\n\nSummary:"
    )
    response = client.chat.completions.create(
        model="gpt-4o",  # Or your preferred model
        messages=[{"role": "user", "content": prompt}],
        max_tokens=100,   # Lower max_tokens for brevity
        temperature=0.2   # Lower temperature for less creative, more straightforward responses
    )
    return response.choices[0].message.content.strip()

# Example usage:
test_text = (
    "Climate change is one of the most significant challenges of our time. "
    "Rising global temperatures have led to extreme weather events, melting polar ice, "
    "and disruptions to ecosystems. Human activities such as deforestation and industrial pollution "
    "have accelerated these changes, and scientists stress the need for immediate action to reduce greenhouse gas emissions."
)

simplified_summary = simplified_summarization_agent(test_text)
print("Simplified Summary:")
print(simplified_summary)
