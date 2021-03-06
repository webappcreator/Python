# itertools.permutations() generates permutations 
# for an iterable. Time to brute-force combinations :)

import itertools
for p in itertools.permutations('ACGT'):
    print(p)
	
# 	('A', 'C', 'G', 'T')
# 	('A', 'C', 'T', 'G')
# 	('A', 'G', 'C', 'T')
# 	('A', 'G', 'T', 'C')
# 	('A', 'T', 'C', 'G')
# 	('A', 'T', 'G', 'C')
# 	('C', 'A', 'G', 'T')
# 	('C', 'A', 'T', 'G')
# 	('C', 'G', 'A', 'T')
# 	('C', 'G', 'T', 'A')
# 	('C', 'T', 'A', 'G')
# 	('C', 'T', 'G', 'A')
# 	('G', 'A', 'C', 'T')
# 	('G', 'A', 'T', 'C')
# 	('G', 'C', 'A', 'T')
# 	('G', 'C', 'T', 'A')
# 	('G', 'T', 'A', 'C')
# 	('G', 'T', 'C', 'A')
# 	('T', 'A', 'C', 'G')
# 	('T', 'A', 'G', 'C')
# 	('T', 'C', 'A', 'G')
# 	('T', 'C', 'G', 'A')
# 	('T', 'G', 'A', 'C')
# 	('T', 'G', 'C', 'A')