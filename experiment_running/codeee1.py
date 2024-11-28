import os
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer
from transformers import T5Tokenizer, T5ForConditionalGeneration
import nltk
from nltk.corpus import wordnet
import torch

# Download WordNet for query expansion
nltk.download('wordnet')
nltk.download('omw-1.4')

# 1. Load text files from the IET faculty directory
def load_texts_from_folders(base_dir):
    text_data = {}
    for root, dirs, files in os.walk(base_dir):
        for file in files:
            if file.endswith(".txt"):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    text_data[file_path] = f.read()
    return text_data

# 2. Generate embeddings for the loaded text files
def generate_embeddings(text_data, model):
    texts = list(text_data.values())  # Extracting just the content of the text files
    embeddings = model.encode(texts)
    return embeddings, texts

# 3. Create FAISS index from the embeddings
def create_faiss_index(embeddings):
    dimension = embeddings.shape[1]  # Get the embedding size (e.g., 384 for Sentence-BERT)
    index = faiss.IndexFlatL2(dimension)  # L2 distance for similarity search
    index.add(np.array(embeddings))  # Add the embeddings to the FAISS index
    return index

# 4. Save and load FAISS index
def save_faiss_index(index, file_path="faiss_index.index"):
    faiss.write_index(index, file_path)
    print(f"FAISS index saved to {file_path}")

def load_faiss_index(file_path="faiss_index.index"):
    index = faiss.read_index(file_path)
    print(f"FAISS index loaded from {file_path}")
    return index

# 5. Query expansion using WordNet
def expand_query_with_synonyms(query):
    expanded_query = set([query])
    for word in query.split():
        for syn in wordnet.synsets(word):
            for lemma in syn.lemmas():
                expanded_query.add(lemma.name().replace('_', ' '))
    return " ".join(expanded_query)

# 6. Search FAISS index for the top-k relevant texts
def search_faiss_index(query, index, texts, model, top_k=5):
    query_embedding = model.encode([query])  # Generate embedding for the query
    distances, indices = index.search(np.array(query_embedding), top_k)  # Perform the search
    relevant_texts = [texts[i] for i in indices[0]]  # Retrieve the top-k matching texts
    return relevant_texts

# 7. Generate a response with T5
def generate_summary_with_t5(context, query, t5_tokenizer, t5_model):
    # Prepare input for summarization or generation
    input_text = f"question: {query} context: {context}"
    inputs = t5_tokenizer.encode(input_text, return_tensors='pt', max_length=512, truncation=True)
    
    # Generate the summary or response
    summary_ids = t5_model.generate(inputs, max_length=150, min_length=50, length_penalty=2.0, num_beams=4, early_stopping=True)
    
    # Decode and return the summary or response
    summary = t5_tokenizer.decode(summary_ids[0], skip_special_tokens=True)
    return summary

# Example: Running the experimental pipeline with IET faculty data

# Step 1: Load a small subset of IET faculty data
base_dir = "faculty_info_iet"  # Directory containing the faculty .txt files
text_data = load_texts_from_folders(base_dir)
print(f"Loaded {len(text_data)} text files from IET faculty.")

# Step 2: Load a pre-trained Sentence-BERT model for embedding generation
model = SentenceTransformer('all-MiniLM-L6-v2')

# Step 3: Generate embeddings for the IET faculty texts
embeddings, texts = generate_embeddings(text_data, model)

# Step 4: Create a FAISS index for the IET faculty texts
index = create_faiss_index(embeddings)

# Step 5: Expand a sample query (optional but useful for improving retrieval)
query = "Tell me about Amit Kumar Sinhal"  # This is a sample query related to a specific faculty member
expanded_query = expand_query_with_synonyms(query)
print(f"Expanded Query: {expanded_query}")

# Step 6: Search the FAISS index for the top 5 relevant texts
relevant_texts = search_faiss_index(expanded_query, index, texts, model, top_k=5)
print(f"Top relevant texts:\n{'-'*40}")
for text in relevant_texts:
    print(f"{text[:200]}...\n{'-'*40}")

# Step 7: Generate a response using T5
# Load the T5 model and tokenizer
t5_tokenizer = T5Tokenizer.from_pretrained('t5-large')
t5_model = T5ForConditionalGeneration.from_pretrained('t5-large')

# Combine the retrieved paragraphs into a single context
context = " ".join(relevant_texts)

# Generate the response using T5
response = generate_summary_with_t5(context, query, t5_tokenizer, t5_model)
print(f"Generated Response:\n{response}")
