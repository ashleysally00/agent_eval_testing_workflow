def evaluate_summary_advanced(generated, reference, expected_keywords):
    # Keyword check (from before)
    missing_keywords = [kw for kw in expected_keywords if kw.lower() not in generated.lower()]
    keyword_passed = len(missing_keywords) == 0
    
    # Semantic similarity
    sim_score = semantic_similarity(generated, reference)
    
    # Readability
    reading_ease, smog = readability_metrics(generated)
    
    results = {
        "keyword_passed": keyword_passed,
        "missing_keywords": missing_keywords,
        "semantic_similarity": sim_score,
        "flesch_reading_ease": reading_ease,
        "smog_index": smog,
    }
    
    return results

# Example advanced evaluation
reference_summary = (
    "Climate change is a major challenge marked by rising temperatures and extreme weather. "
    "Human actions like deforestation and pollution worsen the problem, and scientists urge immediate action to cut emissions."
)
expected_keywords = ["climate change", "global temperatures", "greenhouse gas emissions", "ecosystem", "extreme weather"]
advanced_results = evaluate_summary_advanced(generated_summary, reference_summary, expected_keywords)
print("Advanced Evaluation Results:")
for k, v in advanced_results.items():
    print(f"{k}: {v}")
