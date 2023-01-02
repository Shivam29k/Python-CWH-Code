# Write a program to generate multiplication tables from 2 to 20 and write it to th different files. Place these files in a folder for a 13 year old
for i in range(2, 21):
    f = open(f'tables/table {i}', 'w')
    for j in range(1, 11):
        f.write(f'{i} x {j} = {i*j}')
        if j != 10:
            f.write('\n')
