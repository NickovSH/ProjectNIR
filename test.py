import os


size = os.path.getsize('output.txt')
if size == 0:
    with open('output.txt', 'w') as f:
        f.write('2')

