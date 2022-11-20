#(x,y) seklinde verilen ucgende sonradan verilen (x,y) ikilileri 
#alanin icinde olup olmadigini kontrol eden program
#Ornek: ucgen->(0,0)(0,5)(7,0) aranan nokta->(0,2) result True

def alan_bul(a):
#[A(x1,y1), B(x2,y2) , C(x3,y3)] olan ABC ucgensel bolge alani
#Alan(ABC)= 1/2 | (x1.y2 + x2.y3 + x3.y1) − (y1.x2 + y2.x3 + y3.x1) | 
    return 0.5* abs((a[0][0]*a[1][1] + a[1][0]*a[2][1] + a[2][0]*a[0][1]) - (a[0][1]*a[1][0] + a[1][1]*a[2][0] + a[2][1]*a[0][0]))

def ucgen_mi(ucgen): #basit kontrol
    if ucgen[0][0]==ucgen[1][0] and ucgen[1][0]==ucgen[2][0]:
        return False
    elif ucgen[0][1]==ucgen[1][1] and ucgen[1][1]==ucgen[2][1]:
        return False
    else:
        return True

ucgen=[["",""],["",""],["",""]]

for i in range(3):
    x=int(input(f"x coordinates {i+1}. point:"))
    y=int(input(f"y coordinates {i+1}. point:"))
    ucgen[i][0]=x
    ucgen[i][1]=y
    print("\n")
run=ucgen_mi(ucgen)
if run==False:
    print("boyle bir ucgen yok")

if run==True:
    alan=alan_bul(ucgen)

    kontrol=["",""]
    x=int(input("x coordinates control point:"))
    y=int(input("y coordinates control point:"))
    kontrol[0]=x
    kontrol[1]=y

    #nokta ile ucgeni uc parcaya bol. uc parcanin alanlari=ucgenin alaniysa icinde
    s1=[ucgen[0],ucgen[1],kontrol]
    s2=[ucgen[0],ucgen[2],kontrol]
    s3=[ucgen[1],ucgen[2],kontrol]
    control_alanlari=[s1,s2,s3]
    alanlar=["","",""]
    toplam=0
    for i in range(3):
        alanlar[i]=alan_bul(control_alanlari[i])
    for i in alanlar:
        toplam+=i

    if toplam==alan:
        print(True)
    else:
        print(False)
