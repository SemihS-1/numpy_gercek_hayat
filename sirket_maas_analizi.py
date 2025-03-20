import numpy as np
import matplotlib.pyplot as plt

maaslar = np.random.randint(3000, 15000, 500)
ortalama_maas = np.mean(maaslar)
maksimum_maas = np.max(maaslar)
minimum_maas = np.min(maaslar)
print("Maksimum maaş:", maksimum_maas)

#500 çalışanı 3 farklı departmana rastgele atayın:
#1 = Mühendislik
#2 = Muhasebe
#3 = Pazarlama
#Her departmandaki ortalama maaşı hesaplayın.
departmanlar =np.random.randint(1,4,500)
1 == "Mühendislik"
2 == "Muhasebe"
3 == "Pazarlama"
ortalama_maas_muhendislik = np.mean(maaslar[departmanlar ==1],dtype=int) # Ortalama maaşları simüle ettik ve dtype=int ifadesi ile ortalama maaş değerlerini tam sayı yaptık.
ortalama_maas_muhasebe = np.mean(maaslar[departmanlar == 2],dtype=int)
ortalama_maas_pazarlama = np.mean(maaslar[departmanlar == 3],dtype=int)
print("Ortalama mühendislik maaşı:", ortalama_maas_muhendislik)
print("Ortalama muhasebe maaşı:", ortalama_maas_muhasebe)
print("Ortalama pazarlama maaşı:", ortalama_maas_pazarlama)

plt.figure(figsize=(6,3)) # Burdan itibaren maaş dağılımını gösteren bir histogram çizdik.
plt.hist(maaslar, bins=15, edgecolor="black", alpha=1)
plt.xlabel("Maaşlar")
plt.ylabel("Kişi Sayısı")
plt.title("Maaş Dağılımı")
plt.grid(False)
plt.show()