
import re
 
s = input('Введите слово : ')
d = {'[AEIOULNSTRaeioulnstr]': '1', '[DGdg]': '2', '[BCMPbcmp]': '3', '[FHVWYfhvwt]': '4', 'Kk': '5', '[JXjx]': '8', '[QZqz]': '10',
'[АВЕИНОРСТавенорст]': '1', '[ДКЛМПУдклмпу]' : '2', '[БГЁЬЯбгёья]': '3', '[ЙЫйы]': '4', '[ЖЗХЦЧжзхцч]': '5', '[ШЭЮшэю]': '8', '[ФЩЪфщъ]': '10'}

for k in d:
    s = re.sub(k, d[k], s)
print(sum(map(int, s)))