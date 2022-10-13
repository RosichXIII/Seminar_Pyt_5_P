# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

import codecs

wanton_text = 'Дьтьбв твыьывдлшсабв дмо жчсл абвоабв осл абв дччшчш щсщссщ ваабавб авб бав ропи пщшмщабв'
with codecs.open('Wanton_text.txt', 'w', "utf-16") as File:
    File.write(wanton_text)
fragment = 'абв'
result_text = []
with codecs.open('Wanton_text.txt', 'r', "utf-16") as File:
    for line in File:
        result_text = wanton_text.split()
for i in result_text:
    if fragment in i:
        result_text.remove(i)
with codecs.open('Result_text.txt', 'w', "utf-16") as File:
    for i in result_text:
        File.write(f'{i} ')