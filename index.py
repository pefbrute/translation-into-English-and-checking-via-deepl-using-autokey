import pyperclip
import pyautogui
import time
from googletrans import Translator
import subprocess
import sys

# Constants
SLEEP_TIME_SHORT = 0.1
SLEEP_TIME_MEDIUM = 2
SLEEP_TIME_LONG = 3
VIVALDI_BROWSER_PATH = "vivaldi"
DEEPL_WEBSITE_URL = "https://www.deepl.com/write"
ENGLISH_LANGUAGE_CODE = 'en'

# Check if necessary modules are installed
def check_dependencies():
    required_modules = ["pyperclip", "pyautogui", "googletrans"]
    for module in required_modules:
        if module not in sys.modules:
            print(f"Missing module: {module}. Please install it using pip.")
            sys.exit(1)

def copy_text_to_clipboard():
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(SLEEP_TIME_SHORT)

def get_text_from_clipboard():
    return pyperclip.paste()

def translate_text(input_text, target_language=ENGLISH_LANGUAGE_CODE):
    translator = Translator()
    return translator.translate(input_text, dest=target_language).text

def open_website_in_browser(url):
    subprocess.run([VIVALDI_BROWSER_PATH, url])
    time.sleep(SLEEP_TIME_LONG)

def paste_text():
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(SLEEP_TIME_MEDIUM)

def select_and_copy_all_text():
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(SLEEP_TIME_SHORT)
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(SLEEP_TIME_SHORT)

def close_current_window():
    pyautogui.hotkey('ctrl', 'w')
    time.sleep(SLEEP_TIME_SHORT)

def switch_to_previous_window():
    pyautogui.hotkey('alt', 'tab')
    time.sleep(SLEEP_TIME_SHORT)

def translate_text_to_english_and_paste():
    try:
        copy_text_to_clipboard()
        input_text = get_text_from_clipboard()
        translated_text = translate_text(input_text)

        open_website_in_browser(DEEPL_WEBSITE_URL)

        pyperclip.copy(translated_text)
        paste_text()

        pyautogui.hotkey('tab')
        time.sleep(SLEEP_TIME_SHORT)
        pyautogui.hotkey('tab')

        time.sleep(SLEEP_TIME_MEDIUM)

        select_and_copy_all_text()

        close_current_window()

        switch_to_previous_window()

        paste_text()

    except Exception as e:
        print(f"An error occurred: {e}")

check_dependencies()
translate_text_to_english_and_paste()
