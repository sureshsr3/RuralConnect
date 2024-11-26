# # from flask import Flask, render_template, request
# # import cv2
# # import pytesseract
# # from PIL import Image
# # import spacy
# # import re
# # from indicnlp.tokenize import indic_tokenize
# # from indicnlp.normalize.indic_normalize import IndicNormalizerFactory

# # app = Flask(__name__)

# # # Load English NLP model with entity recognition capabilities
# # nlp = spacy.load("en_core_web_sm")

# # # Function to perform OCR on the image
# # def ocr(image_path):
# #     text = pytesseract.image_to_string(Image.open(image_path))
# #     return text

# # # Function to preprocess the image
# # def preprocess_image(image_path):
# #     img = cv2.imread(image_path)
# #     img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# #     img_thresh = cv2.threshold(img_gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
# #     return img_thresh

# # # Function to extract name of the person using NER
# # def extract_name(text):
# #     doc = nlp(text)
# #     for ent in doc.ents:
# #         if ent.label_ == "PERSON":
# #             return ent.text
# #     return None

# # # Function to extract first date label entity as the date
# # def extract_date(text):
# #     doc = nlp(text)
# #     for ent in doc.ents:
# #         if ent.label_ == "DATE":
# #             return ent.text
# #     return None

# # # Function to extract last second cardinal as grand total amount
# # def extract_grand_total(text):
# #     cardinals = re.findall(r'\d{3}+\.\d{2}', text)
# #     if len(cardinals) >= 2:
# #         grand_total_amount = cardinals[-2]
# #         return grand_total_amount
# #     return None

# # # Function to extract information from different types of documents
# # def extract_information(image_path, document_type):
# #     extracted_text = ocr(image_path)
# from flask import Flask, render_template, request, jsonify
# from document_extraction import extract_electric_bill_info, extract_gas_bill_info, water_bill_extraction_function, insurance_extraction_function, aadhar_card_extraction_function, aadhar_card_back_extraction_function, pan_card_extraction_function, voter_id_extraction_function

# app = Flask(__name__)

# # Route to render the HTML page
# @app.route('/')
# def index():
#     return render_template('index.html')

# # Route to handle the document extraction
# @app.route('/extract', methods=['POST'])
# def extract():
#     selected_option = request.form['documentType']

#     # Check if a file was uploaded  
#     if 'fileInput' not in request.files:
#         return jsonify({'error': 'No file uploaded'})

#     file = request.files['fileInput']

#     # Check if the file is empty
#     if file.filename == '':
#         return jsonify({'error': 'Empty file'})

#     # Check if the selected option is valid
#     if selected_option not in ["electricBill", "gasBill", "waterBill", "insurance", "aadharCard", "aadharCardback", "panCard", "voterId"]:
#         return jsonify({'error': 'Invalid document type'})

#     # Call the appropriate extraction function based on the selected document type
#     if selected_option == "electricBill":
#         output = extract_electric_bill_info(file)
#     elif selected_option == "gasBill":
#         output = extract_gas_bill_info(file)
#     elif selected_option == "waterBill":
#         output = water_bill_extraction_function(file)
#     elif selected_option == "insurance":
#         output = insurance_extraction_function(file)
#     elif selected_option == "aadharCard":
#         output = aadhar_card_extraction_function(file)
#     elif selected_option == "aadharCardback":
#         output = aadhar_card_back_extraction_function(file)
#     elif selected_option == "panCard":
#         output = pan_card_extraction_function(file)
#     elif selected_option == "voterId":
#         output = voter_id_extraction_function(file)
   
#     return render_template('output.html', output=output)


# if __name__ == "__main__":
#     app.run(debug=True)

from indic_transliteration import sanscript
from indic_transliteration.sanscript import transliterate
from flask import Flask, render_template, request, jsonify
from document_extraction import extract_electric_bill_info, extract_gas_bill_info, water_bill_extraction_function, insurance_extraction_function, aadhar_card_extraction_function, aadhar_card_back_extraction_function, pan_card_extraction_function, voter_id_extraction_function
import os
app = Flask(__name__)
from PIL import Image
UPLOAD_FOLDER = 'images/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

global outkan
# Route to render the HTML page
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/kan', methods=['GET','POST'])
def kan():
    outkan=[]
    with open(R"D:\Project\website\tmp.txt", "r+") as tp:
        # for i in tp.readlines():
        # outkan=[i for i in tp.readlines()]
        outkan=[str(transliterate(str(i), sanscript.ITRANS, sanscript.KANNADA)) for i in tp.readlines()]
        print(outkan)
    return render_template('output.html', output=['outkan','g'])


# Route to handle the document extraction
@app.route('/extract', methods=['GET','POST'])
def extract():
    if request.method == 'POST':
        print(f"Form data: {request.form}")
        
        # Debugging statement to inspect the contents of request.files
        print(f"Files: {request.files}")
        file = request.files['file']
        file.save(file.filename)
    
    selected_option = request.form.get('documentType')
    print(f"Selected Document Type: {selected_option}")

    # Check if a file was uploaded  
    # if 'fileInput' not in request.files:
    #     return jsonify({'error': 'No file uploaded'})

    # if request.method == 'POST':  
    #     file = request.files['fileInput']  
    #     file.save(file.filename)
        # f.save(os.path.join(app.config['UPLOAD_FOLDER'], f.'filename'))

    # file = request.files['fileInput'] 
    # print(f"Uploaded File: {file.filename}")

    # Check if the file is empty
    if file.filename == '':
        return jsonify({'error': 'Empty file'})

    # Check if the selected option is valid
    if selected_option not in ["electricBill","Electric Bill", "gasBill", "waterBill", "insurance", "aadharCard", "aadharCardback", "panCard", "voterId"]:
        return jsonify({'error': 'Invalid document type'})
    print(f"Image object: {file}")
    # Call the appropriate extraction function based on the selected document type
    if selected_option == "electricBill":
        ing=file 
        existing_image = Image.open(ing)
        output = extract_electric_bill_info(existing_image)
    elif selected_option == "gasBill":
        ing=file 
        existing_image = Image.open(ing)
        output = extract_gas_bill_info(existing_image)
    elif selected_option == "waterBill":
        ing=file 
        existing_image = Image.open(ing)
        output = water_bill_extraction_function(existing_image)
    elif selected_option == "insurance":
        ing=file 
        existing_image = Image.open(ing)
        output = insurance_extraction_function(existing_image)
    elif selected_option == "aadharCard":
        ing=file 
        existing_image = Image.open(ing)
        output = aadhar_card_extraction_function(existing_image)
    elif selected_option == "aadharCardback":
        ing=file 
        existing_image = Image.open(ing)
        output = aadhar_card_back_extraction_function(existing_image)
    elif selected_option == "panCard":
        ing=file 
        existing_image = Image.open(ing)
        output = pan_card_extraction_function(existing_image)
    elif selected_option == "voterId":
        ing=file 
        existing_image = Image.open(ing)
        output = voter_id_extraction_function(existing_image)
    # with open(R"D:\Project\website\tmp.txt", "w+") as tp:
    #     for i in output:
    #         tp.write(str(i))
    #         tp.write('\n')
    # print(f"Extraction Output: {output}")
    output=[str(transliterate(str(i), sanscript.ITRANS, sanscript.KANNADA)) for i in output]
    print(f"Extraction Output: {output}")
    return render_template('output.html', output=output, document_type=selected_option)
        

if __name__ == "__main__":
    app.run(debug=True)
