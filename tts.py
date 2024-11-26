# from gtts import gTTS
# import os

# # def text_to_speech(text, output_file):
# text="ಣೇತ್ ಆಮೋಉನ್ತ್ ಡುಏ ೧೫೯೯ ಡುಏ ಡತೇ"
# tts = gTTS(text=text, lang='kn', slow=False)  # 'kn' for Kannada
# tts.save(output_file)

from gtts import gTTS
from io import BytesIO
import pygame

def play_text_to_speech(text, lang='kn'):
    # Initialize gTTS
    tts = gTTS(text=text, lang=lang, slow=False)
    
    # Save the speech to a bytes buffer
    audio_bytes = BytesIO()
    tts.write_to_fp(audio_bytes)
    audio_bytes.seek(0)

    # Initialize pygame mixer
    pygame.mixer.init()
    pygame.mixer.music.load(audio_bytes)
    pygame.mixer.music.play()

    # Keep the script running until the speech finishes playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)

# Example usage
if __name__ == "__main__":
    text = "ನಿವ್ವಳ ಮೊತ್ತ ಅಂತಿಮ ದಿನಾಂಕ 799."
    play_text_to_speech(text)
