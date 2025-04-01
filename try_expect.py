try:
  f = open('demofile.txt', 'r')
  print(f.read())
  
except FileNotFoundError:
  print('An exception occurred')

try:
  f = open('myfile.txt', 'w')

  f.write('Hello, world!')
except:
  print('Something went wrong')
finally:
  print('The try except is finished')