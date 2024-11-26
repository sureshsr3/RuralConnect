import spacy
import pytesseract
from PIL import Image
import re

# Load English NLP model with entity recognition capabilities
nlp = spacy.load("en_core_web_sm")

# Function to extract text from an image using OCR
def extract_text_from_image(image_path):
    # Open the image file
    with Image.open(image_path) as img:
        # Use Tesseract OCR to extract text
        language ='kan+eng'
        text = pytesseract.image_to_string(img,lang=language)
    return text

# Sample image path
image_path = "Bescom_Electricity_Bill.jpg"  # Replace with the path to your image

# Extract text from the image
extracted_text = extract_text_from_image(image_path)
print("Extracted Text:")
print(extracted_text)

# Process the extracted text using spaCy NLP
doc = nlp(extracted_text)

# Extract entities of interest
entities = [(ent.text.strip(), ent.label_) for ent in doc.ents]
print("Entities:")
print(entities)

# Define utility document entity types of interest
utility_document_entity_types = ["DATE", "MONEY"]

# Define keywords for relevant entities
relevant_keywords = ["Billing Period","Net Ant.Due", "Due Date", "Net Ant.Due"]

# Filter relevant entities
relevant_entities = []
for text, label in entities:
    for keyword in relevant_keywords:
        if keyword.lower() in text.lower() and label in utility_document_entity_types:
            relevant_entities.append((text, label))
            break

# Print extracted relevant entities
print("Relevant Entities:")
for entity, label in relevant_entities:
    print(f"Entity: {entity}, Label: {label}")
