a = 0
x = 0
y = 0
HP = 0
BL = "None"
TP = "FOP:AIR"
Data = {}
while a<=2600:
    Data["a"+str(a)]={"x":x,"y":y,"HP":HP,"BL":BL,"TP":TP}
    if x == 50:
        y+=1
        x=0
    else:
        x+=1
    a+=1
def add():
    rounda+=1
    if roundb == 5:
        roundb=0
        roundb+=1
    else:
        roundb+=1
rounda = 0
roundb = 0
Data['a1']['TP']="FOP:CORE"
Data['a1']['BL']=1
Data['a1']['HP']=20
Data['a2600']['TP']="FOP:CORE"
Data['a2600']['BL']=2
Data['a2600']['HP']=20
add()
if roundb == 1:
    print('目前回合為A方放兵')
    A_put = input('請輸入要放的兵種ID，不要放的話請輸入cancel')
    if not A_put == 'cancel':
        print('請輸入')
        
