import pandas as pd
import numpy as np

# 1. Sınıfın vize ve final verilerini oluşturma
data = {
    'Ogrenci': ['Ali', 'Ayşe', 'Mehmet', 'Fatma', 'Can', 'Elif', 'Burak'],
    'Vize': [45, 80, 55, 90, 30, 75, 60],
    'Final': [50, 85, 60, 95, 40, 80, 55]
}
df = pd.DataFrame(data)

# 2. Yıl sonu ortalamasını hesaplama (Vize %40, Final %60)
df['Ortalama'] = np.round((df['Vize'] * 0.4) + (df['Final'] * 0.6), 2)

# 3. NumPy ile Çan Eğrisi İstatistikleri
sinif_ortalamasi = np.mean(df['Ortalama'])
std_sapma = np.std(df['Ortalama'])

# 4. Standart sapmaya göre Harf Notu belirleme
kosullar = [
    df['Ortalama'] >= sinif_ortalamasi + std_sapma,
    (df['Ortalama'] >= sinif_ortalamasi) & (df['Ortalama'] < sinif_ortalamasi + std_sapma),
    (df['Ortalama'] >= sinif_ortalamasi - std_sapma) & (df['Ortalama'] < sinif_ortalamasi),
    df['Ortalama'] < sinif_ortalamasi - std_sapma
]
harfler = ['AA', 'BB', 'CC', 'FF']

# ÇÖZÜM: default parametresine string bir değer atadık
df['Harf_Notu'] = np.select(kosullar, harfler, default='Belirsiz')

# 5. Çıktıları Görüntüleme
print("🎓 SINIF NOT DURUMU VE ÇAN EĞRİSİ 🎓\n")
print(f"Sınıf Ortalaması: {sinif_ortalamasi:.2f}")
print(f"Standart Sapma: {std_sapma:.2f}\n")
print("-" * 40)
print(df.to_string(index=False))