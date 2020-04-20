#! python3
# bulletPointAdder.py - Adds Wikipedia bullet points to the start
# of each line of text on the clipboard.

import pyperclip

lines = pyperclip.paste().split('\n')
lines_with_bullets = [f'* {line}' for line in lines]
result = '\n'.join(lines_with_bullets)

pyperclip.copy(result)
