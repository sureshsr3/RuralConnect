# # import pytesseract
# # from PIL import Image
# # import spacy
# # import re

# # # Load English tokenizer, tagger, parser, NER, and word vectors
# # nlp = spacy.load("en_core_web_sm")

# # # Perform OCR on the image
# # def ocr(image_path):
# #     img = Image.open(image_path)
# #     text = pytesseract.image_to_string(img)
# #     return text

# # # NLP processing
# # def extract_information(text):
# #     doc = nlp(text)
# #     name = None
# #     tax_invoice = None
# #     net_payable_amount = None
    
# #     # Named Entity Recognition
# #     for ent in doc.ents:
# #         if ent.label_ == "PERSON":
# #             name = ent.text
# #         elif "tax invoice" in ent.text.lower():
# #             tax_invoice_match = re.search(r'\d{2}-\d{2}-\d{4}', ent.text)
# #             if tax_invoice_match:
# #                 tax_invoice = tax_invoice_match.group()
# #         elif "net payable" in ent.text.lower():
# #             net_payable_match = re.search(r'\d+\.\d{2}', ent.text)
# #             if net_payable_match:
# #                 net_payable_amount = net_payable_match.group()
    
# #     return name, tax_invoice, net_payable_amount

# # # Example usage
# # image_path = "gas.jpg"
# # extracted_text = ocr(image_path)
# # name, tax_invoice, net_payable_amount = extract_information(extracted_text)

# # print("Name:", name)
# # print("Tax Invoice:", tax_invoice)
# # print("Net Payable Amount:", net_payable_amount)
# import cv2
# import pytesseract
# from PIL import Image
# import spacy

# # Load English tokenizer, tagger, parser, NER, and word vectors
# nlp = spacy.load("en_core_web_sm")

# # Perform OCR on the image
# def ocr(image_path):
#     # Preprocess the image
#     img = cv2.imread(image_path)
#     img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     img_thresh = cv2.threshold(img_gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

#     # Save the preprocessed image
#     temp_image_path = "preprocessed_image.png"
#     cv2.imwrite(temp_image_path, img_thresh)

#     # Perform OCR on the preprocessed image
#     text = pytesseract.image_to_string(Image.open(temp_image_path))
#     return text

# # NLP processing
# def extract_information(text):
#     doc = nlp(text)
#     cardinals = []
#     entities = []
#     name = None
#     net_payable_amount = None
#     booking_date = None
    
#     # Named Entity Recognition
#     for ent in doc.ents:
#         entities.append((ent.text, ent.label_))
#         if ent.label_ == "PERSON":
#             name = ent.text
#         elif ent.label_ == "CARDINAL":
#             cardinals.append(ent.text)
    
#     # Extracting the second-to-last CARDINAL entity as net payable amount
#     if cardinals:
#         net_payable_amount = cardinals[-2]
    
#     # Extracting dates using NER
#     dates = [ent.text for ent in doc.ents if ent.label_ == "DATE"]
#     if dates:
#         booking_date = dates[-1]  # Select the last date
    
#     return name, net_payable_amount, booking_date, entities

# # Example usage
# image_path = "gas.jpg"
# extracted_text = ocr(image_path)
# name, net_payable_amount, booking_date, entities = extract_information(extracted_text)

# print("Name:", name)
# print("Net Payable Amount:", net_payable_amount)
# print("Booking Date:", booking_date)
# print("\nEntities:")
# for entity, label in entities:
#     print(f"{entity} - {label}")

import cv2
import pytesseract
from PIL import Image
from indicnlp.tokenize import indic_tokenize
from indicnlp.normalize.indic_normalize import IndicNormalizerFactory
import spacy
import re

# Load English tokenizer, tagger, parser, NER, and word vectors
nlp = spacy.load("en_core_web_sm")

# Perform OCR on the image
def ocr(image_path):
    # Preprocess the image
    img = cv2.imread(image_path)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_thresh = cv2.threshold(img_gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

    # Save the preprocessed image
    temp_image_path = "preprocessed_image.png"
    cv2.imwrite(temp_image_path, img_thresh)

    # Perform OCR on the preprocessed image
    text = pytesseract.image_to_string(Image.open(temp_image_path))
    
    return text
def extract_name(text):
    name_match = re.search(r'Name\s*:\s*(\b[A-Z][a-z]*\b\s*[A-Z]*\s*[A-Z]*\b)', text, re.IGNORECASE)
    if name_match:
        name = name_match.group(1).strip()
        return name
    return None

# NLP processing
def extract_information(text):
    doc = nlp(text)
    cardinals = []
    entities = []
    name = None
    net_payable_amount = None
    booking_date = None
    
    # Named Entity Recognition
    for ent in doc.ents:
        entities.append((ent.text, ent.label_))
        if ent.label_ == "PERSON":
            name = ent.text
        elif ent.label_ == "CARDINAL":
            cardinals.append(ent.text)
    
    # Extracting the second-to-last CARDINAL entity as net payable amount
    if cardinals:
        net_payable_amount = cardinals[-3]
    
    # Extracting dates using NER
    dates = [ent.text for ent in doc.ents if ent.label_ == "DATE"]
    if dates:
        booking_date = dates[-1]  # Select the last date
    
    return  net_payable_amount, booking_date, entities

# Example usage
image_path = "gas1.jpg"
extracted_text = ocr(image_path)

# Tokenize the extracted text using Indic NLP Library
factory = IndicNormalizerFactory()
normalizer = factory.get_normalizer("hi")
tokens = indic_tokenize.trivial_tokenize(normalizer.normalize(extracted_text), lang='hi')

# Reconstruct the text from tokens
extracted_text = ' '.join(tokens)

net_payable_amount, booking_date, entities = extract_information(extracted_text)
text=ocr(image_path)
name=extract_name(text)
print("GAS BILL")

print("Name:", name)
print("Net Payable Amount:", net_payable_amount)
print("Booking Date:", booking_date)


