from itertools import permutations
import os

s = input("Hier Wort eingeben: ").lower()
permuts = permutations(s)
o = open("output.txt", "w", encoding="utf-8")
e = open("ergebnis.txt", "w", encoding="utf-8")
for i in list(permuts):
    print (''.join(i), file=o)
o.close()


list1 = [line.rstrip('\n') for line in open("output.txt", "r", encoding="utf-8")]
list2 = [line.rstrip('\n') for line in open("dict.txt", "r", encoding="utf-8")]
for i in list1:
    if i in list2:
        print('Wort gefunden: "'+i+'"')
        os.system("pause")
        print('Wort gefunden: "'+i+'"', file=e)
        break
else:
    print("Nichts gefunden")
    os.system("pause")
    print('Nichts gefunden', file=e)

"""
with open('output.txt', 'r', encoding="utf-8") as file1:
    with open('dict.txt', 'r',encoding="utf-8") as file2:
        for i in file1:
            if i in file2:                
                print("gefunden")
                print("Wort ist: " + i)
                break
            else:
                print("nicht gefunden")
                break
"""
"""
        same = set(file1).intersection(file2)

same.discard('\n')

for line in same:
    print(line.lower(), file=e)
"""
e.close()
o.close()
open("output.txt", "w").close()
