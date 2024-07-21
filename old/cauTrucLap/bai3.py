# input: so ga so cho sao cho chan ga + chan cho  =100 va ga + cho = 36
# output: so ga so cho

for ga in range(37) :
  if ((ga * 2 + (36 - ga) * 4) == 100):
   print('Số gà =', ga,'con')
   print('Số chó =', 36 - ga,'con')

