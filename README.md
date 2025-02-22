
# Agentic Workflow Evaluation: Text Summarization Agent

*****still working on this rewrite later****************

## Overview
This project contains a simple workflow for *evaluating AI agents.* The goal is to systematically assess and refine an AI agent's performance by testing, analyzing outputs, adjusting parameters, and retesting. This example implements a **text summarization agent** using:

* **OpenAI API** for text summarization
* **Transformers library** for semantic similarity analysis

## Project Structure
* `agent.py` → Initial implementation of the text summarization agent
* `test_workflow.py` → First round of testing with sample inputs
* `metrics.py` → Evaluation metrics, including semantic similarity and readability
* `readability.py` → Calculates readability scores
* `semantic_similarity.py` → Computes semantic similarity between original text and summaries
* `edited_parameters.py` → Adjusted agent settings after analyzing initial results
* `edited_eval.py` → Retesting after modifying agent behavior

## Step 1: Initial Test & Results

Input Text:
```
Climate change is a major contemporary challenge, characterized by rising global temperatures that cause extreme weather, melting ice, and ecosystem disruptions. Human activities like deforestation and industrial pollution exacerbate these effects. Scientists stress the urgency of reducing greenhouse gas emissions to mitigate environmental impacts.
```

Initial Summary Output:
```
Climate change leads to extreme weather, melting ice, and ecosystem disruptions. Human activities worsen the problem. Scientists urge reducing emissions.
```

### Evaluation Metrics:
* **Semantic Similarity Score:** 0.90
* **Flesch Reading Ease:** -2.68 (complex)
* **SMOG Index:** 16.30 (difficult to read)

### Observations:
* The summary retained key points but was still complex
* The readability score indicated high difficulty
* The agent needed adjustments for more accessible summaries

## Step 2: Adjusting Parameters & Retesting

### Modifications:
1. Adjusted **temperature** and **max_tokens** to simplify language
2. Applied **post-processing** for clarity

New Summary Output:
```
Climate change is a big problem today. It causes higher temperatures, extreme weather, and melting ice. This affects nature and wildlife. Human actions like cutting down trees and pollution make it worse. Scientists say we must act now to cut down on greenhouse gases.
```

### New Evaluation Metrics:
* **Semantic Similarity Score:** 0.88
* **Flesch Reading Ease:** 71.00 (easy to read)
* **SMOG Index:** 7.60 (much simpler language)

### Observations:
* The summary remained accurate while becoming **more readable**
* **Better balance** between information retention and accessibility
* The **agent was successfully refined** through iterative testing

## Key Takeaways
This project demonstrates how to evaluate an **agentic AI workflow** using a structured testing process:

1. **Generate initial outputs** → Assess AI performance
2. **Measure metrics** → Semantic similarity, readability, etc.
3. **Identify areas for improvement** → Adjust prompts, parameters, or processing
4. **Retest and compare** → Observe performance changes

This approach is useful for **any AI-driven agent**, from summarization to decision-making systems, ensuring continuous improvement and alignment with intended objectives.

## How to Use This Project

### Clone the Repository
```
git clone https://github.com/ashleysally00/agent_eval_testing_workflow.git
cd agent_eval_testing_workflow
```

### Run Initial Test
```
python test_workflow.py
```

### Evaluate Outputs
```
python metrics.py
```

### Modify Parameters & Retest
```
python edited_parameters.py
python edited_eval.py
```

## Conclusion

This workflow offers a clear method for testing and refining AI agents. By using evaluation metrics and making iterative improvements, we can enhance their performance and create more user-friendly AI outputs.
