**Overview**

This text improvement model is designed to enhance text quality by analyzing and augmenting its semantic content. Utilizing state-of-the-art NLP techniques, the model assesses text input for improvements, making it more coherent, semantically rich, and contextually relevant.

**Setup**
_Prerequisites_
Python 3.x
pip


__Installation__
Clone the repository to your local machine.
Navigate to the project directory.

Install the required dependencies by running:

pip install transformers torch numpy scipy gradio

**Why we use them?**

Transformers: To use pre-trained NLP model.
Torch: Utilized for tensor operations.
NumPy & SciPy: For numerical and scientific computations.
Gradio: To create an interactive web interface for easy model testing.

I used "sentence-transformers/all-MiniLM-L6-v2" model from Hugging Face's Transformers library for semantic analysis.

**Usage**
To use the model, run the provided script. This will launch a Gradio interface in your web browser to input text.

Result

<img width="1125" alt="Screenshot 2024-02-01 at 8 05 41 PM" src="https://github.com/GoingLight/text_improvement/assets/48763973/8293851a-1a8e-4467-a3e7-e5e18e82be0a">



**Limitations**
The model's performance is dependent on the quality and training of NLP model used. Results may vary based on the complexity and specificity of the text input. Also the list of standardized phrases should be updated with wide range of word combinations to get higher quality results. 
