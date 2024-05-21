from unstructured.partition.pdf import partition_pdf
import os
import json

pdf_path = "cookbook.pdf"

def write_list(file, filename):
    print("Started writing list data into a json file")
    with open(filename, "w") as fp:
        json.dump(file, fp)
        print("Done writing JSON data into .json file")

# Load and partition the PDF using the unstructured library
document = partition_pdf(
    filename = pdf_path,
    chunking_strategy = 'by_title',
    max_characters = 1500,
    new_after_n_chars = 1500,
    combine_text_under_n_chars = 250,
    extract_images_in_pdf = False,
    infer_table_structure=True,
    strategy="hi_res");

text_chunks = []
tables = []

# Process the document elements
for element in document:
    if "unstructured.documents.elements.Table" in str(type(element)):
        tables.append(str(element))
    elif "unstructured.documents.elements.CompositeElement" in str(type(element)):
        text_chunks.append(str(element))

write_list(text_chunks, 'text_chunks.json')
write_list(tables, 'tables.json')