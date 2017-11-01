import random
import time
f = open("data","a+")

while True:
  a = random.randint(0,51)
  b = random.randint(0,51)
  s = ''
  s += str(a)+','+str(b)
  print(s)
  f.write(s)
  f.write('\n')
  time.sleep(1)