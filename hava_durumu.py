import numpy as np
import matplotlib.pyplot as plt

sicakliklar = np.random.randint(-10,41,365) #Bir yıl boyunca (365 gün) günlük sıcaklık değerlerini simüle edin. Sıcaklıklar -10°C ile 40°C arasında rastgele belirlenecek.
ortalama_sicaklik = np.mean(sicakliklar, dtype=int) #Ortalama sıcaklığı bulun.
en_soguk_gun = np.min(sicakliklar) #En sıcak günü bulun.
en_sicak_gun = np.max(sicakliklar) #En soğuk günü bulun.
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
