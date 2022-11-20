#recursive
def faktoriyel(sayi):
    if sayi==1 or sayi==0:
        return 1 
    else:
        return sayi*faktoriyel(sayi-1)
    
sayi=int(input("faktoriyeli alinacak sayi giriniz:"))
print(faktoriyel(sayi))

"""
#faktoriyel
sayi=int(input("recursive degil test:"))
i=1
sonuc=1
while i<=sayi:
    sonuc*=i
    i+=1
print(sonuc)
"""
