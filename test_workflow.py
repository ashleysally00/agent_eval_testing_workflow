import os
from dotenv import load_dotenv
from openai import OpenAI
import time

# Load environment variables from .env
load_dotenv()

# Instantiate the client with your API key
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def summarization_agent(text):
    """
    Sends a summarization prompt to an LLM using the new ChatCompletion interface.
    """
    prompt = f"Please summarize the following text in a concise manner:\n\n{text}\n\nSummary:"
    response = client.chat.completions.create(
        model="gpt-4o",  # Or use another model like "gpt-3.5-turbo"
        messages=[{"role": "user", "content": prompt}],
        max_tokens=150,
        temperature=0.3
    )
    return response.choices[0].message.content.strip()

def evaluate_summary(summary, expected_keywords):
    """
    Evaluates a generated summary by checking if all expected keywords appear.
    Returns a tuple of (passed: bool, missing_keywords: list).
    """
    missing = [kw for kw in expected_keywords if kw.lower() not in summary.lower()]
    return (len(missing) == 0, missing)

def run_evaluation_workflow():
    # Define a list of test cases with literary texts and the keywords you expect in their summaries.
    test_cases = [
        {
            "text": (
                "In the golden haze of a setting sun, the gentle murmur of the waves mingled with the soft whispers of the wind. "
                "Every ripple carried a tale of forgotten dreams and distant lands, while the sky, painted in hues of amber and rose, "
                "seemed to cradle the hopes of a thousand hearts, inviting a moment of quiet introspection and wonder."
            ),
            "expected_keywords": ["sunset", "waves", "nature", "beauty", "introspection"]
        },
        {
            "text": (
                "Beneath the sprawling canopy of ancient trees, the forest exhaled a symphony of life. "
                "Birdsong and the rustling of leaves blended into a chorus that spoke of resilience and renewal, "
                "reminding wanderers of the eternal dance between growth and decay."
            ),
            "expected_keywords": ["forest", "life", "birds", "resilience", "renewal"]
        },
        # Add more test cases as needed
    ]

    # Iterate over each test case, generate a summary, evaluate it, and log the results.
    for i, case in enumerate(test_cases, start=1):
        print(f"\n--- Test Case {i} ---")
        print("Input Text:\n", case["text"])
        start_time = time.time()
        summary = summarization_agent(case["text"])
        duration = time.time() - start_time
        print("\nGenerated Summary:\n", summary)
        passed, missing = evaluate_summary(summary, case["expected_keywords"])
        if passed:
            print("Result: Test Passed!")
        else:
            print("Result: Test Failed. Missing keywords:", missing)
        print(f"Response Time: {duration:.2f} seconds")

# Run the evaluation workflow
if __name__ == "__main__":
    run_evaluation_workflow()
