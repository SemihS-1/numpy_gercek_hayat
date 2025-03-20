import numpy as np
import matplotlib.pyplot as plt

ürünler = ["Telefon", "Bilgisayar", "Kulaklık", "Saat", "Tablet"] # Ürünlerin adları: "Telefon", "Bilgisayar", "Kulaklık", "Saat", "Tablet". 
satislar = np.random.randint(10,101,(5,30)) # 5 farklı ürün için 30 günlük rastgele satış değerleri üretin (10-100 arası değişebilir). 
toplam_satislar = np.sum(satislar, axis=1) # Her ürünün toplam satış miktarlarını hesaplayın.
ortalama_satislar = np.mean(satislar, axis=1, dtype=int) # Her ürünün ortalama satış miktarlarını hesaplayın.
for ürün in ürünler:
    print(f"{ürün} için toplam satış: {toplam_satislar[ürünler.index(ürün)]}, ortalama satış: {ortalama_satislar[ürünler.index(ürün)]}")

plt.figure(figsize=(8,4)) # Ürün bazında bir çubuk grafiği çizin.
plt.bar(ürünler, toplam_satislar, color="orange")
plt.xlabel("Ürünler")
plt.ylabel("Satış Miktarları")
plt.title("Ürün Satışları")
plt.show()