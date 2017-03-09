money = input("Net value" '\n')
code = input("Total cost" '\n')

def difference():
  a = float(float(money) - float(code))
  b = int((a%1)*100)
  a = int(a)
  
  print ('%s dollars' % a,'and', '%s cents' % b )
  
difference()
