# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

import random
import string
example_text = []
for i in range(random.randint(5, 10)):
    letter = random.choice(string.ascii_letters)
    for j in range(1, random.randint(6, 9)):
        example_text.append(letter)
with open('Example_text.txt', 'w') as File:
    File.write(''.join(example_text))

encoded_text = []
count = 1
with open('Example_text.txt', 'r') as File:
    for line in File:
        for i in range(len(line) - 1):
            if line[i] == line[i + 1]:
                count +=1
            else:
                encoded_text.append(str(count) + line[i])
                count = 1
        if line[-2] != line[-1] or count > 1:
            encoded_text.append(str(count) + line[i])    
print('Результат кодировки:',''.join(encoded_text))

decoded_text = []
number = 0
for i in encoded_text:
    for j in i:
        if j.isdigit():
            number = int(j)
        else:
            decoded_text.append(j * number)
            number = 0
with open('Decoded_text.txt', 'w') as File:
    File.write(''.join(decoded_text))    