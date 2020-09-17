a = 0
x = 0
y = 0
HP = 0
BL = "None"
TP = "FOP:AIR"
temp_list=[]
Data = {}
class rangetest():
    global temp_list,Data
    def __init__(格子1,格子2):
        global temp_list,Data
        return(abs((((int(格子1[x]))-(int(格子2[x])))**2)+(((int(格子1[y]))-(int(格子2[y])))**2)))
    def all_block_check(中心格,半徑):
        global temp_list,Data
        temp_list=[]
        test_count=0
        while test_count<=2600:
            temp_data=rangetest(Data["a"+test_count],Data["a"+test_count])
            if temp_data<=半徑:
                temp_list=temp_list+["a"+test_count]
            test_count+=1
            return(temp_list)
def blockscheck(回合擁有人):
    global Data,temp_list
    temp_list=[]
    for a in Data:
        if Data[a]['BL']==回合擁有人:
            temp_list = temp_list+[a]
            return(temp_list)
            
while a<=2600:
    Data["a"+str(a)]={"x":x,"y":y,"HP":HP,"BL":BL,"TP":TP}
    if x == 50:
        y+=1
        x=0
    else:
        x+=1
    a+=1
rounda=0
roundb=0
def add():
    global rounda,roundb
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
        print(blockscheck(2))
