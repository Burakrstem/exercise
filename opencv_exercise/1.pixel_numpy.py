#genellikle 8-bpp(8 bit per pixel) olarak depolanir. her pixelin 256 gri seviye tonu burdan gelir
#renkli resimlerin her pixel kanalinda rgb 256 tonu tutulur. 
#maskeleme yaparak 2 seviye degerine dusurme==>siyah255 beyaz0

#acık kaynak kodlu
#c++ python java ... destekli
#windows,linux


#numerical python
import numpy as np

dizi=np.array([1,2,3,4,5,6.945],dtype='i')
#hepsini tek veri tipinde tutar

print(dizi)
print(type(dizi))
print(type(dizi.dtype))
print("dizi boyut:",dizi.ndim)
print("dizi.shape:",dizi.shape)
print("toplam eleman sayisi:",dizi.size,end="\n\n")

#matrisler(cok boyutlu diziler) de tanimlanabilir
matris= np.array([[1,2,3],
                [4,5,6],
                [7,8,9]])
print(matris)
print("matris boyut:",matris.ndim)
print("matris.shape:",matris.shape)
print("matris.size:",matris.size,end="\n\n")


print("0 matris=",np.zeros(3),end="\n\n")
print("1 matris=\n",np.ones((3,3)),end="\n\n")
print("birim matris=\n",np.eye((3)),end="\n\n")
print("tum degerler 25 olsun=\n",np.full(3,25),end="\n\n")
print("10 20 arasi random 3*2 matris=\n",np.random.randint(10,20,(3,2)),end="\n\n")



