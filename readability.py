import textstat

def readability_metrics(text):
    flesch_reading_ease = textstat.flesch_reading_ease(text)
    smog_index = textstat.smog_index(text)
    return flesch_reading_ease, smog_index

# Define or generate a summary first
generated_summary = (
    "Climate change is a major contemporary challenge, characterized by rising global temperatures "
    "that cause extreme weather, melting ice, and ecosystem disruptions. Human activities like deforestation "
    "and industrial pollution exacerbate these effects. Scientists stress the urgency of reducing greenhouse gas emissions "
    "to mitigate environmental impacts."
)

reading_ease, smog = readability_metrics(generated_summary)
print(f"Flesch Reading Ease: {reading_ease:.2f}")
print(f"SMOG Index: {smog:.2f}")
