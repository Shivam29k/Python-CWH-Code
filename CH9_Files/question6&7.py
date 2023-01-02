content = True
i = 0
with open('log.txt') as f:
    while content:
        i += 1
        content = f.readline()

        if 'python' in content.lower():
            print(content)
            print(f'yes python is present in line no {i}')
