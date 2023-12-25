import time
import os
import pyperclip
print("Program uruchomiony")

last_data = pyperclip.paste()

while True:
    try:
        clipboard_data = pyperclip.paste()
        if clipboard_data != last_data:
            with open("schowek.txt", 'a') as f:
                print(clipboard_data)
                f.write(clipboard_data + '\n')
            last_data = clipboard_data
    except Exception as e:
        print(f'Error: {str(e)}')
    time.sleep(0.5)
