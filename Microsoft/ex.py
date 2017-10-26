f = open('Keys').read()
keys = f.split('\n')

key = []
for i in keys:
  res = i.split(',')
  for j in res:
    key.append(j)