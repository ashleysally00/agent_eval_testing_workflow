from edited_parameters import simplified_summarization_agent
import textstat

def readability_metrics(text):
    """
    Computes readability metrics using textstat.
    """
    flesch_reading_ease = textstat.flesch_reading_ease(text)
    smog_index = textstat.smog_index(text)
    return flesch_reading_ease, smog_index

def evaluate_simplified_summary():
    # Define your test input text
    test_text = (
        "Climate change is one of the most significant challenges of our time. "
        "Rising global temperatures have led to extreme weather events, melting polar ice, "
        "and disruptions to ecosystems. Human activities such as deforestation and industrial pollution "
        "have accelerated these changes, and scientists stress the need for immediate action to reduce greenhouse gas emissions."
    )
    
    # Generate the simplified summary
    summary = simplified_summarization_agent(test_text)
    print("Simplified Summary:")
    print(summary)
    
    # Evaluate the readability of the generated summary
    reading_ease, smog = readability_metrics(summary)
    print(f"\nFlesch Reading Ease: {reading_ease:.2f}")
    print(f"SMOG Index: {smog:.2f}")

if __name__ == "__main__":
    evaluate_simplified_summary()
