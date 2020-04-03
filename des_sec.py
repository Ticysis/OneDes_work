
def text_name_encode(textenc): #string to bin
    enc =[]
    enc2=[]  
    textenc = textenc + " "
#    with open(textenc + ".txt", "r", encoding="utf-8") as isim:
    chars = []
#        for line in isim:
    for c in textenc:
        chars.append(c)
    
    enc1 = [bin(ord(i))[2:].zfill(8) for i in chars]
    enc2=enc1[:-1]
    strEnc2=''.join(enc2)
    enc3=strEnc2.split()
    strEnc3=' '.join([strEnc2[x:x+8] for x in range(0,len(strEnc2), 8)])

    return strEnc3

def XOR(one,two):
    try:
        len(one) == len(two)
    except Exception:
        print('异或长度异常')
    Rest = ''
    for i in len(one):
        if one[i] == two[i]:
            Rest = Rest + '0'
        else:
            Rest += '1'
    return Rest

def Zhi_Huan(rule,strs):
    Resmus = ""
    for i in rule:
#    print("源数字是:"+inits[i-1])
        Resmus = Resmus + strs[i-1]
    return Resmus
#=======================================================   





 
#           8       16          24      32      40      48      56          64
inits = "0011001000110000001110100110010001100101011100110011001100110010"
#                  8       16          24      32      40      48      56         64
#inits_other = "00110010 00110000 00111010 01100100 01100101 01110011 00110011 00110010"

k1 = [57,49,41,33,25,17,9, #7
      1,58,50,42,34,26,18, #14
      10,2,59,51,43,35,27, #21
      19,11,3,60,52	,44,36,#28
      63,55,47,39,31,23,15,#35
      7,62,54,46,38,30,22, #42
      14,6,61,53,45	,37,29,#49
      21,13,5,28,20,12,4]  #56
k2 = [14,17,11,24,1,5,
      3,28,15,6,21,10,
      23,19,12,4,26,8,
      16,7,27,20,13,2,
      41,52,31,37,47,55,
      30,40,51,45,33,48,
      44,49,39,56,34,53,
      46,42,50,36,29,32,]
newinits = ""
for i in k1:
#    print("源数字是:"+inits[i-1])
    newinits = newinits + inits[i-1]
print('======================第一次置换============================')
print("K1筛选后为: "+newinits)

print('======================分为左右============================')
C0 = newinits[:28]
#print('C01:'+C0[:7]+' '+C0[7,14]+' '+C0[14,21]+' '+C0[21,28])
D0 = newinits[28:]

print("C0: "+C0+"\n"+"D0: "+D0+"\n")

#左移 
C_all = []
D_all = []

for i in range(17):
    tmp = C0[i:]+C0[:i]
    print("第"+str(i)+"位C"+str(i)+": \t"+tmp)
    C_all.append(tmp)

for i in range(17):
    tmp = D0[i:]+D0[:i]
    print("第"+str(i)+"位D"+str(i)+": \t"+tmp)
    D_all.append(tmp)

new_Ks = []

for i in range(17):
    tmp = C_all[i]+D_all[i]
    print("新KEY(new_Ks"+str(i)+"): "+tmp)
    new_Ks.append(tmp)

Fn_dict_Keys = {}
ins = 0
for i in new_Ks:
    tmp = ""
    print("当前变换为["+str(ins)+"]: "+str(i))
    ins += 1
    for s in k2:
        tmp = tmp + i[s-1]
    print("结果为:"+tmp)
    Fn_dict_Keys[i] = tmp

print(new_Ks[16])




#=======================================================
#Enums = input('输入>>> ')
Enums = '80460132'
Dig_Enums = text_name_encode(Enums)
print('生成的二进制数为>>> '+Dig_Enums)
Dig_NoS_Enums = Dig_Enums.replace(' ','')
print('去除空格>>> '+Dig_NoS_Enums)


IP_First = [58,50,42,34,26,18,10,2,
60,52,44,36,28,20,12,4,
62,54,46,38,30,22,14,6,
64,56,48,40,32,24,16,8,
57,49,41,33,25,17,9,1,
59,51,43,35,27,19,11,3,
61,53,45,37,29,21,13,5,
63,55,47,39,31,23,15,7]

first_IP = ''

for i in IP_First:
    first_IP = first_IP + Dig_NoS_Enums[i-1]
print('======================第一次Ip置换============================')
print("K1筛选后为: "+first_IP)
L0 = first_IP[:32]
R0 = first_IP[32:]
print('\n分为L0和R0:\nL0>>> '+L0+'\nR0>>> '+R0)

Ext_B = [32,1,2,3,4,5,
4,5,6,7,8,9,
8,9,10,11,12,13,
12,13,14,15,16,17,
16,17,18,19,20,21,
20,21,22,23,24,25,
24,25,26,27,28,29,
28,29,30,31,32,1]

Ext_R0 = ''

for i in Ext_B:
    Ext_R0 = Ext_R0 + R0[i-1]

Str_ExtR0 = str(Ext_R0)
lens = len(Str_ExtR0)
print('\nExtR0的长度为:'+str(lens)+'\nExtR0的结果为: '+Ext_R0)










#S盒置换
S1 = []






Final_rules = [40,8,48,16,56,24,64,32,
39,7,47,15,55,23,63,31,
38,6,46,14,54,22,62,30,
37,5,45,13,53,21,61,29,
36,4,44,12,52,20,60,28,
35,3,43,11,51,19,59,27,
34,2,42,10,50,18,58,26,
33,1,41,9,49,17,57,25 ]