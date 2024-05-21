# Retrieval Augmented Generation pipeline using pretrained LLM
Shuvadeep Saha

This project showcases a Retrieval Augmented (RAG) pipeline using Gemini-7B-it LLM from HuggingFace. 
The steps to train the RAG pipeline is as follows:

Step-1: The pdf (a cookbook manual) was preprocessed to extract the sentence chunks using the `unstructured` library. The text was chunked depending on the max character length or depending on the heading and sub-heading.

Step-2: From the extracted chunks of sentences/paragraphs, create a embedding search database using the `faiss` vector search database. The similarity score adopted was cosine similarity with approximate nearest neighbor search technique. This vector databased contained the indexing of the 768-dimensional embeddings for each text chunk.

Step-3: Whenever a user query is submitted, the pipeline retrieves the most relevant text chunks from the pdf file and these text chunks are provided to the LLM as the context. The LLM then augments its response to generated a domain-specific response that is directly taken from the pdf. The code snippet of the generation is shown below:

![image](https://github.com/shuvanyu/Retrieval-Augmented-Generation-RAG/assets/91404954/ffe06d21-340f-4f84-a51b-58866381277c)


## Steps to ask a question to the RAG LLM:
1. install `generation_requirements.txt`
2. Go to `RAG-pipeline.ipynb`.
3. Type the desired query.
4. Run the file

-----------------------
## Steps to replicate the enire training and generation pipeline:
## Training
1. install `training_requirements.txt`
2. Get the pdf / pdfs.
3. Run the `extract.py`. This will save the text chunks in `text_chunks.json` file.
4. Run the `store_embeddings.py` which will use faiss to index and store the embeddings in a vector database name `embeddings.index` file.
   
The training of the RAG pipeline is over. Now we focus on `Generation` and `Augmentation`.

## Generation and Augmentation:
1. install `generation_requirements.txt`
2. Run the `base_prompt.py` file. You may make the necessary changes in the prompt depending on the domain of the pdf
3. Run the `prompt_formatter.py` file.
4. Run the `import_LLM.py` that imports the Gemini-7B-it model from HuggingFace. Use your unique HuggingFace access token in place of `HF_TOKEN` in the code.
5. Run the `get_answer.py`
6. Run the `RAG-pipeline.ipynb` with desired query

