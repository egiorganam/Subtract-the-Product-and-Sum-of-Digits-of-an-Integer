
def subtractProductAndSum(n):
  string_number = str(n)
  print(type(string_number))

  list_number = list(string_number)
  print(list_number)

  product = 1
  sum = 0
  
  for i in list_number:
    j = int(i)
    product *= j
    sum += j

  """sum = 0
  for i in list_number:
    j = int(i)
    sum += j"""

  print(product - sum)
  

subtractProductAndSum(234)
subtractProductAndSum(4421)