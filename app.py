from transformers import AutoTokenizer, AutoModel
import torch
from scipy.spatial.distance import cosine
import gradio as gr

tokenizer = AutoTokenizer.from_pretrained("sentence-transformers/all-MiniLM-L6-v2")
model = AutoModel.from_pretrained("sentence-transformers/all-MiniLM-L6-v2")

standard_phrases = [
    "Optimal performance", "Utilise resources", "Enhance productivity", "Conduct an analysis",
    "Maintain a high standard", "Implement best practices", "Ensure compliance", "Streamline operations",
    "Foster innovation", "Drive growth", "Leverage synergies", "Demonstrate leadership",
    "Exercise due diligence", "Maximize stakeholder value", "Prioritise tasks", "Facilitate collaboration",
    "Monitor performance metrics", "Execute strategies", "Gauge effectiveness", "Champion change"
]

def get_embedding(text):
    tokens = tokenizer(text, padding=True, truncation=True, return_tensors="pt")
    with torch.no_grad():
        output = model(**tokens)
    return torch.mean(output.last_hidden_state, dim=1).squeeze()

def calculate_similarity(embedding1, embedding2):
    return 1 - cosine(embedding1, embedding2)

def suggest_improvements(input_text):
    input_phrases = [phrase.strip() for phrase in input_text.split('.') if phrase]  
    suggestions = []
    for phrase in input_phrases:
        phrase_embedding = get_embedding(phrase)
        best_match = ("", 0)  
        for standard_phrase in standard_phrases:
            standard_embedding = get_embedding(standard_phrase)
            similarity = calculate_similarity(phrase_embedding.numpy(), standard_embedding.numpy())
            if similarity > best_match[1]:  
                best_match = (standard_phrase, similarity)
        if best_match[1] > 0.5:  
            suggestions.append(f"Original: '{phrase}' - Suggested: '{best_match[0]}' (Similarity: {best_match[1]:.2f})")
    return "\n".join(suggestions) if suggestions else "No significant improvements found."


def gradio_interface(text):
    suggestions = suggest_improvements(text)
    return suggestions if suggestions else "Your text is already good enough!"

iface = gr.Interface(fn=gradio_interface,
                     inputs="text_area",
                     outputs="text",
                     title="Text Improvement Tool",
                     description="Enter your text...")

if __name__ == "__main__":
    iface.launch(debug=True)

