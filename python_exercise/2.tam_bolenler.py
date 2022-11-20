sayi=int(input("tam bolenlerinin bulunacagi sayiyi gir:"))

tam_bolenler=[]
i=1
while i<=sayi:
    if sayi % i==0:
        tam_bolenler.append(i)
    i+=1


for i in range (len(tam_bolenler)):
    print(f"{i+1}. tam bolen==>{tam_bolenler[i]}")
