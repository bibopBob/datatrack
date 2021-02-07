local = 1
visit = 1

my_list = [ 1, 2, 3, 4]

new_val = 0
for item in my_list:
    new_val = local + item

def showme(some,bool_val=False):
    if bool_val : print(some)
    return some

def sumarLista(num,lista):
  result = 0
  for item in lista:
    result += num + item
  return result
