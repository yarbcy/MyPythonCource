def count_sheeps(arrayOfSheeps):
  count_sheeps = 0
  for item in arrayOfSheeps:
      if item == 'True' or item == True:
          count_sheeps += True
  return count_sheeps