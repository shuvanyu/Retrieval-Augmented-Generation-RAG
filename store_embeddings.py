import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
import torch
from read_json import read_list

device = 'cuda' if torch.cuda.is_available() else 'cpu'

embed_model = SentenceTransformer('all-mpnet-base-v2', device = device)
text_chunks = read_list('text_chunks.json')

# DataLoader
text_chunk_embeddings = embed_model.encode(text_chunks,
                                           convert_to_tensor = True,
                                           show_progress_bar = True,
                                           batch_size = 32)

# Define dimensionality and number of clusters
d = text_chunk_embeddings.shape[1]  # Embedding dimension
nlist = 100  # Number of clusters

# Create the index
quantizer = faiss.IndexFlatL2(d)  # The quantizer for the clustering
index = faiss.IndexIVFFlat(quantizer, d, nlist, faiss.METRIC_INNER_PRODUCT)

# Train the index
index.train(text_chunk_embeddings.to('cpu'))

# Add the embeddings to the index
index.add(text_chunk_embeddings.to('cpu'))

# Save the index table to file:
faiss.write_index(index, 'embeddings.index')