import numpy as np
#listelere benzer

matris=np.array([[1,2,3,55,56,57],
                 [4,5,6,58,59,60]])

print(matris,end="\n\n")

#1.satir 2.sutun elemanini degis
matris[0,1]=25
print(matris,end="\n\n")

#2.satir [2.elemandan 5.elemana) kadar al
print(matris[1,1:4],end="\n\n")

for eleman in matris:
    print(eleman)

print("\n\n")

for satir in matris:
    for eleman in satir: 
        print(eleman)


print("\n\n")

print(np.where(matris==56))  
print("\n\n")

#filtreleme
print(matris<20)
print("\n\n")

yeni_matris=matris[matris<20]
print(yeni_matris)