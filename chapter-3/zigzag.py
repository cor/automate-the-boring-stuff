import time
import sys

# CONFIGURATION
WIDTH = 30
INDENT_STEP = 2
SPEED = 50

# Current State
indent = 0  # How many spaces to indent
indent_increasing = True

try:
    while True:
        print(' ' * indent, end='')
        print('********')
        time.sleep(1 / SPEED)

        if indent_increasing:
            indent += INDENT_STEP
            if indent == WIDTH:
                indent_increasing = False  # Change direction

        else:
            indent -= INDENT_STEP
            if indent == 0:
                indent_increasing = True   # Change direction

except KeyboardInterrupt:
    sys.exit()

