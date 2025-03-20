import numpy as np
import matplotlib.pyplot as plt

sicakliklar = np.random.uniform(-10,41,365) #Bir yıl boyunca (365 gün) günlük sıcaklık değerlerini simüle edin. Sıcaklıklar -10°C ile 40°C arasında rastgele belirlenecek.
np.round(sicakliklar, 2) #Sıcaklık değerlerini 2 ondalık basamağa yuvarlayın.
ortalama_sicaklik = round(np.mean(sicakliklar),2) #Ortalama sıcaklığı bulun. Virgülden sonrakı 2 basamağı gösterin
en_soguk_gun = round(np.min(sicakliklar),2) #En sıcak günü bulun.
en_sicak_gun = round(np.max(sicakliklar),2) #En soğuk günü bulun.
print("Ortalama sıcaklık:", ortalama_sicaklik, "Derece")
print("En soğuk gün:", en_soguk_gun, "Derece")
print("En sıcak gün:", en_sicak_gun, "Derece")
plt.figure(figsize=(8,2))
plt.plot(sicakliklar, color="red", linestyle="solid") #Sıcaklık değişimlerini çizgi grafiği ile gösterin
plt.xlabel("Günler")
plt.ylabel("Sıcaklık Değerleri")
plt.title("Sıcaklık Değişimleri")
plt.grid(False)
plt.show()
