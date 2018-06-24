from collections import Counter
valid_matrix = ["....5..1.",
				".4.3.....",
				".....3..1",
				"8......2.",
				"..2.7....",
				".15......",
				".....2...",
				".2.9.....",
				"..4......" ]


rows = [list(i) for i in valid_matrix] 

cols=[]
for i in range(0,len(valid_matrix)):
    cols.append([valid_matrix[j][i] for j in range(0, len(valid_matrix[i]))])

subs = []
for i in range(0,9,3):
    for k in range(0,9,3):
        subs.append(list(''.join([j[k:k+3] for j in valid_matrix[i:i+3]])))
l =[rows,cols,subs]
def isValid(l):
    for rec in l:
        for row in rec:
            if [item for item, count in Counter(list(row)).iteritems() if count > 1] !=['.']:
                return 0

print isValid(l)