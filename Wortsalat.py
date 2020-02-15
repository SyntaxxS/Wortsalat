from itertools import permutations 

s = input()
permuts = permutations(s)
for perm in list(permuts):
         print (''.join(perm))