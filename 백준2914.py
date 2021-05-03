import math
my_list=  (input().split(" "))
b= list(map(float,my_list))
c= math.ceil(b[0])
d= math.ceil(b[1])
print(c*(d-1)+1)


