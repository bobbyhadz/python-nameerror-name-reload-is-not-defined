# NameError: name 'reload' is not defined in Python

import glob
import importlib

new = importlib.reload(glob)

print(new) # 👉️ <module 'glob' (built-in)>