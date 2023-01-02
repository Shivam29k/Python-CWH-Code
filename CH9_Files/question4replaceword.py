# A file contains a word 'donkey' mu;tiple times. you need to write  program to replace this word with ####### by updating the same file

words = ['mota', 'donkey', 'sala', 'chutiya']

with open('donkey.txt') as f:
    content = f.read()

for word in words:
    content = content.replace(word, '######')
    with open('donkey.txt', 'w') as f:
        f.write(content)
