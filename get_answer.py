# Perform a search
import faiss
from sentence_transformers import SentenceTransformer
import torch

def get_answer(query, device):
    embed_model = SentenceTransformer('all-mpnet-base-v2') #, device = device)
    
    # Load the saved dindex table from file:
    index = faiss.read_index('embeddings.index')

    query_embedding = embed_model.encode(query, convert_to_tensor = True)
    query_embedding = torch.reshape(query_embedding, (1,-1)).to('cpu')
    query_embedding = query_embedding.numpy()
    D, I = index.search(query_embedding, k=5)  # Search for 5 nearest neighbors
    #print(f"Distances: {D}, Indices: {I}")
    
    return I[0]