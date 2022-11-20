"""
cv2.imread(arg1,arg2)=istenilen dosya yolundaki goruntu istenilen formatta yuklenir
cv2.IMREAD_COLOR:varsayilan secenektir. goruntuyu BGR formatinda yukler bayrak degeri 1dir
cv2.IMREAD_UNCHANGED:goruntu oldugu gibi yuklenir. bayrak degeri -1
cv2.IMREAD_GRAYSCALE:goruntuyu gri seviye goruntu olarak yukler bayrak degeri 0 dir

imge.shape=goruntunun satir,sutun,kanal sayisi(renkli goruntude) belirtir
imge.size=goruntudeki toplam pixel sayisi
imge.dtype=goruntu verii tipi
cv2.imshow(arg1,arg2): goruntu gosterilir. ilk arguman gosterilecek pencere basligi
                    ikinci arguman gosterilecek goruntu
cv2.waitKey(arg):milisaniye cinsinden pencerenin acik kalmasi gereken sure
                0 yazilirsa pencere kapatilana kadar acik kalir
"""

import cv2 
#print (cv2.__version__)
imge=cv2.imread("/home/brk2004/Desktop/python/opencv/red_point.png")

print(imge.shape) #697 satir 1024 sütun 3 kanal(renkli)
print(imge.size)  #toplam pixel sayisi
print(imge.dtype) #uint8




#sag ust kısmımda 50*50 pixellik bolumu beyazlastır
#for i in range (50):
#    for j in range(50):
#        imge[i,j]=[255,255,255]
#ya da 
#imge[0:50,0:50]=[255,255,255]

roi=imge[250:600,250:600] 
cv2.imshow("Roi",roi)
cv2.imwrite("roi.png",roi)

cv2.imshow("Goruntu",imge)
cv2.waitKey(0)
"""5 saniye sonra kapanmasi icin
cv2.waitkey(5000)
cv2.DestroyAllWindows()
"""