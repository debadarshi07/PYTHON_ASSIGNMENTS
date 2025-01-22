# This is a single line comment.
'''This is a multiline comment'''
"""This can also be used for multiline comments"""
# 'pip' is the package manager for python.
# Two types of modules : Built in Modules(pre-installed), External Modules(need to install using pip)
# External Modules can be installed using pip install <module_name> command in terminal.

import pyjokes as pj, pyttsx3 as ptx, os # This is how importing modules looks like

print('Hello Debadarshi Omkar')
print('''Hello ! Welcome to Python Course.
This is a way to write multiline strings.''')

joke = pj.get_joke()
print(joke)

engine = ptx.init()
engine.say("Hello! How are you ? I'm Debadarshi Omkar.")
engine.runAndWait()

directory_path = '/Users/USER/Documents/'
folders = os.listdir(directory_path)

print('Items in directory are follows:')
for item in folders:
    print(item)