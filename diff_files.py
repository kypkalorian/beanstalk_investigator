import difflib

with open('file1.json') as f1:
    f1_text = f1.read()
with open('file2.json') as f2:
    f2_text = f2.read()
# Find and print the diff:
for line in difflib.unified_diff(f1_text.splitlines(), f2_text.splitlines(), fromfile='file1.json', tofile='file2.json', lineterm=''):
    print(line)