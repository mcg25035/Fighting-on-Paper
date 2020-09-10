a = 0
x = 0
y = 0
Data = {}
while a<=2500:
  Data["a"+str(a)]={"x":x,"y":y}
	if x == 50:
		y+=1
		x=0
	x+=1
