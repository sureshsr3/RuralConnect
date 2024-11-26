# import cv2
# import pytesseract
# from PIL import Image
# import spacy
# import re

# # Load English tokenizer, tagger, parser, NER, and word vectors
# nlp = spacy.load("en_core_web_sm")

# # Perform OCR on the image
# def ocr(image_path):
#     text = pytesseract.image_to_string(Image.open(image_path))
#     return text

# # Extract name of the person using NER
# def extract_name(text):
#     doc = nlp(text)
#     for ent in doc.ents:
#         if ent.label_ == "PERSON":
#             return ent.text
#     return None

# # Extract first date label entity as the date
# def extract_date(text):
#     doc = nlp(text)
#     for ent in doc.ents:
#         if ent.label_ == "DATE":
#             return ent.text
#     return None

# # Extract last second cardinal as grand total amount
# def extract_grand_total(text):
#     cardinals = re.findall(r'\d+\.\d{2}', text)
#     if len(cardinals) >= 2:
#         grand_total_amount = cardinals[-2]
#         return grand_total_amount
#     return None

# # Print OCR output and entities with labels
# def print_ocr_entities(text):
#     doc = nlp(text)
#     print("OCR Output:")
#     print(text)
#     print("\nEntities and Labels:")
#     for ent in doc.ents:
#         print(f"{ent.text} - {ent.label_}")

# # Example usage
# image_path = "dataset/ins4.jpg"
# extracted_text = ocr(image_path)
# name = extract_name(extracted_text)
# date = extract_date(extracted_text)
# grand_total_amount = extract_grand_total(extracted_text)

# print("Name:", name)
# print("Date:", date)
# print("Grand Total Amount:", grand_total_amount)

# # Print OCR output and entities with labels
# print_ocr_entities(extracted_text)

import cv2
import pytesseract
from PIL import Image
import spacy
import re

# Load English tokenizer, tagger, parser, NER, and word vectors
nlp = spacy.load("en_core_web_sm")

# Perform OCR on the image
def ocr(image_path):
    text = pytesseract.image_to_string(Image.open(image_path))
    return text

# Preprocess the image
def preprocess_image(image_path):
    img = cv2.imread(image_path)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_thresh = cv2.threshold(img_gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    return img_thresh

# Extract name of the person using NER
def extract_name(text):
    doc = nlp(text)
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            return ent.text
    return None

# Extract first date label entity as the date
def extract_date(text):
    doc = nlp(text)
    for ent in doc.ents:
        if ent.label_ == "DATE":
            return ent.text
    return None

# Extract last second cardinal as grand total amount
def extract_grand_total(text):
    cardinals = re.findall(r'\d{3}+\.\d{2}', text)
    if len(cardinals) >= 2:
        grand_total_amount = cardinals[-2]
        return grand_total_amount
    return None

# Print OCR output and entities with labels
def print_ocr_entities(text):
    doc = nlp(text)
    print("OCR Output:")
    print(text)
    print("\nEntities and Labels:")
    for ent in doc.ents:
        print(f"{ent.text} - {ent.label_}")

# Example usage
image_path = "dataset/ins1.jpg"

# Preprocess the image
preprocessed_image = preprocess_image(image_path)
cv2.imwrite("preprocessed_image.jpg", preprocessed_image)

# Perform OCR on the preprocessed image
extracted_text = ocr("preprocessed_image.jpg")
name = extract_name(extracted_text)
date = extract_date(extracted_text)
grand_total_amount = extract_grand_total(extracted_text)
print("INSURANCE COPY")
print("Name:", name)
print("Date:", date)
print("Grand Total Amount:", grand_total_amount)

# Print OCR output and entities with labels
print_ocr_entities(extracted_text)
