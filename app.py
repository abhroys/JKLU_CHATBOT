import os
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer
from langchain.vectorstores import FAISS
import nltk
import streamlit as st
import requests
from nltk.corpus import wordnet
from nltk import pos_tag, word_tokenize
import pickle

nltk.download('wordnet')
nltk.download('omw-1.4')
nltk.download('punkt')

def load_single_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()

def load_files_from_folder(folder_path):
    file_data = {}
    for filename in os.listdir(folder_path):
        if filename.endswith('.txt'):  
            file_path = os.path.join(folder_path, filename)
            text = load_single_file(file_path)
            file_data[filename] = text
    return file_data

def split_text_into_chunks(text, max_length=1000):
    sentences = nltk.sent_tokenize(text)
    chunks = []
    current_chunk = ""

    for sentence in sentences:
        if len(current_chunk) + len(sentence) + 1 <= max_length:
            current_chunk += " " + sentence
        else:
            chunks.append(current_chunk.strip())
            current_chunk = sentence
    if current_chunk:
        chunks.append(current_chunk.strip())
    return chunks

def split_text_into_qa_pairs(text):
    pairs = text.split("\n\n")
    qa_pairs = []
    for pair in pairs:
        if "Q:" in pair and "A:" in pair:
            qa_pairs.append(pair.strip())
        else:
            print(f"Warning: Skipping invalid pair: {pair}")
    return qa_pairs

def generate_embeddings(data, model):
    embeddings_dict = {}
    for filename, items in data.items():
        valid_items = [item for item in items if item.strip()]
        if valid_items:
            embeddings = model.encode(valid_items)
            embeddings_dict[filename] = embeddings
    return embeddings_dict

def create_combined_faiss_index(qa_embeddings_dict, scraped_embeddings_dict):
    qa_embeddings = np.vstack(list(qa_embeddings_dict.values()))
    scraped_embeddings = np.vstack(list(scraped_embeddings_dict.values()))
    combined_embeddings = np.vstack([qa_embeddings, scraped_embeddings])
    dimension = combined_embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(combined_embeddings)
    return index

def expand_query_with_synonyms(query):
    expanded_query = set([query])
    words = word_tokenize(query)
    tagged_words = pos_tag(words)
    for word, tag in tagged_words:
        if tag.startswith('NN'):
            for syn in wordnet.synsets(word):
                for lemma in syn.lemmas():
                    expanded_query.add(lemma.name().replace('_', ' '))
    return " ".join(expanded_query)

def concatenate_documents(documents, max_length=2048):
   
    combined_content = ""
    current_length = 0

    for doc in documents:
        doc_length = len(doc['content'].split())  # Approximate token count by word count
        if current_length + doc_length > max_length:
            break  # Stop adding documents once the max length is reached
        combined_content += doc['content'] + " "
        current_length += doc_length

    print(f"Final concatenated content length: {current_length} tokens.")
    return combined_content.strip()  # Return the combined content

def search_faiss(query, index, index_mapping, model, top_k=10):
    query_embedding = model.encode([query])
    distances, indices = index.search(np.array(query_embedding), top_k)
    relevant_docs = {}
    for idx, distance in zip(indices[0], distances[0]):
        if idx < len(index_mapping):
            full_doc = index_mapping[idx].get('doc_name', 'unknown_doc')
            similarity = 1 / (1 + distance)
            if full_doc not in relevant_docs:
                relevant_docs[full_doc] = {'similarity': similarity, 'chunks': []}
            relevant_docs[full_doc]['chunks'].append(index_mapping[idx]['content'])
    full_document_contents = []
    for doc_name, info in relevant_docs.items():
        full_content = "\n".join(info['chunks'])
        full_document_contents.append({'doc_name': doc_name, 'content': full_content, 'similarity': info['similarity']})
    return full_document_contents

def query_groq_api(query, context, api_key, model="llama3-70b-8192"):
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }
    data = {
        'messages': [
            {'role': 'system', 'content': 'You are a helpful assistant.'},
            {'role': 'user', 'content': f"{query}\n\n{context}"}
        ],
        'model': model
    }
    response = requests.post('https://api.groq.com/openai/v1/chat/completions', json=data, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error: {response.status_code}, Message: {response.text}")
        return None



def main():
    st.title("JKLU Chatbot")

    # Load the data, index, and index_mapping
    with st.spinner('Loading precomputed embeddings and FAISS index...'):
        # Load precomputed embeddings from pickle files
        with open("qa_embeddings.pkl", "rb") as f:
            qa_embeddings = pickle.load(f)
        with open("scraped_embeddings.pkl", "rb") as f:
            scraped_embeddings = pickle.load(f)

        # Load the FAISS index
        index = faiss.read_index("faiss_index.index")

        # Check if the `index_mapping` exists, otherwise create and save it
        index_mapping_file = "index_mapping.pkl"
        if os.path.exists(index_mapping_file):
            # Load the saved index_mapping
            with open(index_mapping_file, "rb") as f:
                index_mapping = pickle.load(f)
            #st.write("Index mapping loaded from file.")
        else:
            # Process the Q&A and scraped documents to create the mapping
            qna_folder = "all_structured_qa_files"
            scraped_folder = "all_extracted_files"

            # Load the Q&A and scraped files
            qna_files = load_files_from_folder(qna_folder)
            scraped_files = load_files_from_folder(scraped_folder)

            # Process Q&A and scraped files
            qa_data = {filename: split_text_into_qa_pairs(text) for filename, text in qna_files.items()}
            scraped_doc_chunks = {filename: split_text_into_chunks(text) for filename, text in scraped_files.items()}

            # Create the index mapping
            index_mapping = []
            for filename, qa_pairs in qa_data.items():
                for qa in qa_pairs:
                    index_mapping.append({'type': 'qa', 'doc_name': filename, 'content': qa})
            for doc_name, chunks in scraped_doc_chunks.items():
                for chunk in chunks:
                    index_mapping.append({'type': 'scraped', 'doc_name': doc_name, 'content': chunk})

            # Save the index_mapping for future use
            with open(index_mapping_file, "wb") as f:
                pickle.dump(index_mapping, f)
            st.write("Index mapping created and saved to file.")


    model = SentenceTransformer('all-MiniLM-L12-v2') 
    # User input query
    query = st.text_input("Enter your query")

    if query:
        # Search FAISS index with the query
        expanded_query = expand_query_with_synonyms(query)  # Expand query with synonyms
        full_docs = search_faiss(expanded_query, index, index_mapping, model)  # Use None for model, as embeddings are precomputed
        combined_context = concatenate_documents(full_docs)

        # Groq API call
        api_key = st.secrets["gpt_api_key"]  # Add API key securely in Streamlit
        response = query_groq_api(query, combined_context, api_key)

        if response:
            #st.write("Generated Response:")
            st.write(response['choices'][0]['message']['content'])

if __name__ == '__main__':
    main()