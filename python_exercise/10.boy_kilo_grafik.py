from matplotlib import pyplot as plt

#10 adet ogrenciye ait veriler(boy kilo) girin verileri grafik olarak çizdirin
kilo=[55,60,65,70,75,80,85,90,95,90]
boy=[160,155,170,190,185,175,176,177,165,160]

plt.plot(kilo,boy,linestyle='--',marker='o')
plt.title("kilo-boy grafiği")
plt.xlabel("kilo")
plt.ylabel("boy")

plt.show()

