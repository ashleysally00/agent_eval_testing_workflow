import os
from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables from .env
load_dotenv()

# Instantiate the client with your API key
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def summarization_agent(text):
    """
    Sends a summarization prompt to an LLM using the new ChatCompletion interface.
    """
    prompt = f"Please summarize the following text:\n\n{text}\n\nSummary:"
    response = client.chat.completions.create(
        model="gpt-4o",  # Or another model like "gpt-3.5-turbo"
        messages=[{"role": "user", "content": prompt}],
        max_tokens=100,
        temperature=0.3
    )
    return response.choices[0].message.content.strip()

def evaluate_summarization():
    test_text = (
        "Climate change is one of the most significant challenges of our time. "
        "Rising global temperatures have led to extreme weather events, melting polar ice, "
        "and disruptions to ecosystems. In addition, human activities such as deforestation "
        "and industrial pollution have accelerated these changes. Scientists emphasize the need "
        "for immediate action to reduce greenhouse gas emissions and mitigate the impact on the environment."
    )
    
    # Define expected keywords for a good summary
    expected_keywords = ["climate change", "global temperatures", "greenhouse gas emissions", "environment"]
    
    summary = summarization_agent(test_text)
    print("Generated Summary:\n", summary)
    
    if all(keyword.lower() in summary.lower() for keyword in expected_keywords):
        print("Test Passed: The summary covers key points.")
    else:
        print("Test Failed: The summary may be missing some key information.")

# Run the evaluation
evaluate_summarization()
