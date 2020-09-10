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
def attack(self_block,block,attackr):
	global tmp_attack_list,Data
	if abs(int(((int(Data[block][x])-int(Data[self_block][x]))**2)+((int(Data[block][y])-int(Data[self_block][y]))**2)))<=int(attackr):
		tmp_attack_list=tmp_attack_list+[block]
