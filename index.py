import pyperclip
import pyautogui
import time
from googletrans import Translator
import subprocess
import sys

# Check if necessary modules are installed
def check_dependencies():
    try:
        import pyperclip
        import pyautogui
        import googletrans
    except ImportError as e:
        print(f"Missing module: {e.name}. Please install it using pip.")
        sys.exit(1)

check_dependencies()

translator = Translator()

def translate_text_to_english_and_paste():
    try:
        # Copy selected text
        pyautogui.hotkey('ctrl', 'c')  # Use 'command' instead of 'ctrl' on macOS
        time.sleep(0.1)  # Allow time for clipboard to update

        # Get the text from the clipboard
        input_text = pyperclip.paste()

        # Translate the text
        translated_text = translator.translate(input_text, dest='en').text

        # Open Vivaldi browser with DeepL
        subprocess.run(["vivaldi", "https://www.deepl.com/write"])
        time.sleep(3)  # Wait for the browser to open

        # Paste the translated text
        pyperclip.copy(translated_text)
        pyautogui.hotkey('ctrl', 'v')
        
        time.sleep(3)
        
        pyautogui.hotkey('tab')
        pyautogui.hotkey('tab')
        
        time.sleep(2)
        
        pyautogui.hotkey('ctrl', 'a')
        
        time.sleep(2)
        
        pyautogui.hotkey('ctrl', 'c')
        
        time.sleep(2)
        
        pyautogui.hotkey('ctrl', 'w')
        
        time.sleep(0.5)
        
        pyautogui.hotkey('alt', 'tab')
        
        time.sleep(1)        
        
        pyautogui.hotkey('ctrl', 'v')

    except Exception as e:
        print(f"An error occurred: {e}")

translate_text_to_english_and_paste()
