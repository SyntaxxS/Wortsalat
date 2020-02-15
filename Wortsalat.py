from itertools import permutations


s = input()
permuts = permutations(s)
f = open("output.txt", "w")
for i in list(permuts):
    print (''.join(i), file=f)
f.close()