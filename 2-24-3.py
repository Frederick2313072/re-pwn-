from z3 import *
s=Solver()
v,w,x,y,z=Ints('v w x y z') #定义整数变量
s.add(v * 23 + w * -32 + x * 98 + y * 55 + z * 90 == 333322)
s.add(v * 123 + w * -322 + x * 68 + y * 67 + z * 32 == 707724)
s.add(v * 266 + w * -34 + x * 43 + y * 8 + z * 32 == 1272529)
s.add(v * 343 + w * -352 + x * 58 + y * 65 + z * 5 == 1672457)
s.add(v * 231 + w * -321 + x * 938 + y * 555 + z * 970 == 3372367)
s.check()
print(s.model())