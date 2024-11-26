import spacy
import pytesseract
from PIL import Image
import re

def extract_electric_bill_info(image):
    # Your code to extract information from an electric bill image goes here

    

# Load English NLP model with entity recognition capabilities
    nlp = spacy.load("en_core_web_sm")

# Function to extract text from an image using OCR
    
    # Open the image file
    # with Image.open(image_path) as img:
        # Use Tesseract OCR to extract text
    language ='kan+eng'
    text = pytesseract.image_to_string(image,lang=language)
    

# Sample image path
    image_path = "dataset\Bescom_Electricity_Bill.jpg"  # Replace with the path to your image

# Extract text from the image
    extracted_text = text
    print(extracted_text)
# Process the extracted text using spaCy NLP
    doc = nlp(extracted_text)

# # Extract entities of interest
# entities = [(ent.text.strip(), ent.label_) for ent in doc.ents]
# print("surehs")
# print(entities)
# # Define utility document entity types of interest
# utility_document_entity_types = ["DATE", "MONEY"]

# # Define keywords for relevant entities
# relevant_keywords = ["Billing Period","Subsidy","PERSON", "Due Date", "Total Amount Due"]

# # Filter relevant entities
# relevant_entities = []
# for text, label in entities:
#     for keyword in relevant_keywords:
#         if keyword.lower() in text.lower() and label in utility_document_entity_types:
#             relevant_entities.append((text, label))
#             break

# # Print extracted relevant entities
# for entity, label in relevant_entities:
#     print(f"Entity: {entity}, Label: {label}")
# net_amount_due_match = re.search(r'Net Ant\.Due:(.*?)\n', extracted_text)
    net_amount_due_match = re.search(r'Net Ant\. Due:|NET AMOUNT DUE(.*?)\n', extracted_text, flags=re.IGNORECASE)
    net_amount_due = net_amount_due_match.group(1).strip() if net_amount_due_match else None

# Extracting date   
    dates = re.findall(r'\d{2}/\d{2}/\d{4}|\d{2}-\d{2}-\d{4}', extracted_text)

# Selecting the last date
    last_date = dates[-2] if dates else None


    print("ELECTRIC BILL")
    print("Net Amount Due:", net_amount_due)
    print("Due Date:", last_date)
    return [net_amount_due,last_date]


def extract_gas_bill_info(image):
    

    
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

    # Preprocess the image
    # img = cv2.imread(image_path)
    # img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # img_thresh = cv2.threshold(img_gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

    # # Save the preprocessed image
    # temp_image_path = "preprocessed_image.png"
    # cv2.imwrite(temp_image_path, img_thresh)
    # existing_image = Image.open(temp_image_path)
    # Perform OCR on the preprocessed image
    text = pytesseract.image_to_string(image)
    
    

    name_match = re.search(r'Name\s*:\s*(\b[A-Z][a-z]*\b\s*[A-Z]*\s*[A-Z]*\b)', text, re.IGNORECASE)
    if name_match:
        name = name_match.group(1).strip()
    else: return None

# NLP processing

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
    
   

# Example usage
    
    extracted_text = text 

# Tokenize the extracted text using Indic NLP Library
    factory = IndicNormalizerFactory()
    normalizer = factory.get_normalizer("hi")
    tokens = indic_tokenize.trivial_tokenize(normalizer.normalize(extracted_text), lang='hi')

# Reconstruct the text from tokens
    extracted_text = ' '.join(tokens)


    
    
    print("GAS BILL")

    print("Name:", name)
    print("Net Payable Amount:", net_payable_amount)
    print("Booking Date:", booking_date)

    return [name,net_payable_amount,booking_date]





def water_bill_extraction_function(image):
    
    
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

    # Preprocess the image
    # img = cv2.imread(image_path)
    # img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # img_thresh = cv2.threshold(img_gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

    # Save the preprocessed image
    # temp_image_path = "preprocessed_image.png"
    # cv2.imwrite(temp_image_path, img_thresh)

    # Perform OCR on the preprocessed image
    text = pytesseract.image_to_string(image)
    
    

    name_match = re.search(r'Consumer\s+Details\s*\n*([^0-9]+)', text, re.IGNORECASE)
    if name_match:
        name = name_match.group(1).strip()
        return name
    

# NLP processing

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
        net_payable_amount = cardinals[-2]
    
    # Extracting dates using NER
    dates = [ent.text for ent in doc.ents if ent.label_ == "DATE"]
    if dates:
        booking_date = dates[-3]  # Select the last date
    
    

    net_amount_due_match = re.search(r'Net Amount Due(?:\s*:)?\s*(\d+\.\d{2})', text)
    if net_amount_due_match:
        net_amount_due = net_amount_due_match.group(1)
        return net_amount_due
    

# Example usage
    image_path = "wat1.jpg"
    extracted_text = text

# Tokenize the extracted text using Indic NLP Library
    factory = IndicNormalizerFactory()
    normalizer = factory.get_normalizer("hi")
    tokens = indic_tokenize.trivial_tokenize(normalizer.normalize(extracted_text), lang='hi')

# Reconstruct the text from tokens
    extracted_text = ' '.join(tokens)

    

    
    
    
    
    print("WATER BILL")
    print("Name:", name)
    print("Net Amount Due:", net_amount_due)
    print("Due Date:", booking_date)


    return [name,net_amount_due,booking_date]





def insurance_extraction_function(image):
    
    
    import cv2
    import pytesseract
    from PIL import Image
    import spacy
    import re

# Load English tokenizer, tagger, parser, NER, and word vectors
    nlp = spacy.load("en_core_web_sm")

# Perform OCR on the image

    text = pytesseract.image_to_string(image)
    

# Preprocess the image

    
    # img_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # img_thresh = cv2.threshold(img_gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    

# Extract name of the person using NER

    doc = nlp(text)
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            name= ent.text
    

# Extract first date label entity as the date

    doc = nlp(text)
    for ent in doc.ents:
        if ent.label_ == "DATE":
            date= ent.text
    

# Extract last second cardinal as grand total amount

    cardinals = re.findall(r'\d{3}+\.\d{2}', text)
    if len(cardinals) >= 2:
        grand_total_amount = cardinals[-2]
        
    

# Print OCR output and entities with labels

    doc = nlp(text)
    print("OCR Output:")
    print(text)
    print("\nEntities and Labels:")
    for ent in doc.ents:
        print(f"{ent.text} - {ent.label_}")

# Example usage
    image_path = "dataset/ins1.jpg"

# Preprocess the image
    # preprocessed_image = img_thresh
    # cv2.imwrite("preprocessed_image.jpg", preprocessed_image)

# Perform OCR on the preprocessed image
    extracted_text = text

    
    print("INSURANCE COPY")
    print("Name:", name)
    print("Date:", date)
    print("Grand Total Amount:", grand_total_amount)
    return [name,date,grand_total_amount]

# Print OCR output and entities with labels
    



def aadhar_card_extraction_function(image):
    
    pass





def aadhar_card_back_extraction_function(image):
    pass
def pan_card_extraction_function(image):
    pass

def voter_id_extraction_function(image):
    pass