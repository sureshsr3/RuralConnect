# # # from transformers import MarianMTModel, MarianTokenizer
# # # import torch
# # # import sentencepiece as spm


# # # # Load pre-trained model and tokenizer for English to Kannada translation
# # # model_name = "Helsinki-NLP/opus-mt-en-kn"
# # # tokenizer = MarianTokenizer.from_pretrained(model_name)
# # # model = MarianMTModel.from_pretrained(model_name)

# # # # English text to translate
# # # english_text = "Hello, how are you?"

# # # # Tokenize the input text
# # # inputs = tokenizer(english_text, return_tensors="pt", padding=True, truncation=True)

# # # # Translate the input text to Kannada
# # # with torch.no_grad():
# # #     outputs = model.generate(**inputs, max_length=128, num_beams=4, early_stopping=True)

# # # # Decode the translated text
# # # kannada_text = tokenizer.decode(outputs[0], skip_special_tokens=True)

# # # print("English Text:", english_text)
# # # print("Kannada Translation:", kannada_text)


# # from transformers import MarianMTModel, MarianTokenizer
# # import torch

# # # Load pre-trained model and tokenizer for English to Kannada translation
# # model_name = "Helsinki-NLP/opus-mt-en-kn"
# # tokenizer = MarianTokenizer.from_pretrained(model_name)
# # model = MarianMTModel.from_pretrained(model_name)

# # # English text to translate
# # english_text = "Hello, how are you?"

# # # Tokenize the input text
# # inputs = tokenizer(english_text, return_tensors="pt", padding=True, truncation=True)

# # # Translate the input text to Kannada
# # with torch.no_grad():
# #     outputs = model.generate(**inputs, max_length=128, num_beams=4, early_stopping=True)

# # # Decode the translated text
# # kannada_text = tokenizer.decode(outputs[0], skip_special_tokens=True)

# # print("English Text:", english_text)
# # print("Kannada Translation:", kannada_text)


# from transformers import MarianMTModel, MarianTokenizer
# import torch


# # Load pre-trained model and tokenizer for English to Kannada translation
# model_name = "ai4bharat/indic-trans-en-kn"
# tokenizer = MarianTokenizer.from_pretrained(model_name)
# model = MarianMTModel.from_pretrained(model_name)

# # Example translation
# english_text = "Hello, how are you?"
# inputs = tokenizer(english_text, return_tensors="pt", padding=True, truncation=True)

# with torch.no_grad():
#     outputs = model.generate(**inputs, max_length=128, num_beams=4, early_stopping=True)

# kannada_translation = tokenizer.decode(outputs[0], skip_special_tokens=True)
# print("Kannada Translation:", kannada_translation)
from indic_transliteration import sanscript
from indic_transliteration.sanscript import transliterate

# Sample text in English
text = "Net Amount Due 1599"

# Transliterate to Kannada
kannada_text = transliterate(text, sanscript.ITRANS, sanscript.KANNADA)
print(kannada_text)

# Sample text in English
text_date = "Due Date"

# Transliterate to Kannada
kannada_text_date = transliterate(text_date, sanscript.ITRANS, sanscript.KANNADA)
print(kannada_text_date)
