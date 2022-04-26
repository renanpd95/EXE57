import os

x = int(input("Digite o primeiro número: "))
y = int(input("Digite o segundo número: "))
z = int(input("Digite o terceiro número: "))

os.system('clear')


if (x > y and x > z ):
  print ("O maior entre eles é:",x)
elif (y > z and y > x ):
  print ("O maior entre eles é:",y)
elif (z > x and z > y ):
  print ("O maior entre eles é:",z)
  